#!/usr/bin/env bash

set -eu

THIS_SCRIPT="$(readlink -f "${0}")"
THIS_DIR="$(dirname "${THIS_SCRIPT}")"
ROOT_DIR="$(dirname "${THIS_DIR}")"
RUN="poetry -C "${THIS_DIR}" run"
DOCS_GEN="${THIS_DIR}"
CONFIGS="${DOCS_GEN}/configurations"

gen_spec () {
    SPEC_ROOT="${ROOT_DIR}/$(jq -r '.root' "${CONFIGS}/$1")"
    echo "Spec root folder: ${SPEC_ROOT}"

    TARGET_CLASS="$(jq -r '.targetclass' "${CONFIGS}/$1")"
    echo "Target class: ${TARGET_CLASS}"

    SCHEMA_FILE="$(jq -r '.schemafile' "${CONFIGS}/$1")"
    echo "Schema file: ${SCHEMA_FILE}"

    EXAMPLES_DIR="${SPEC_ROOT}/examples/valid"
    echo "Examples folder: ${EXAMPLES_DIR}"
    for EXAMPLE in $(ls "${EXAMPLES_DIR}"/*-0*.yaml) ; do
        echo "Validate example: ${EXAMPLE}"
         ${RUN} linkml validate \
            --schema "${SPEC_ROOT}/${SCHEMA_FILE}" \
            --target-class "${TARGET_CLASS}" \
            "${EXAMPLE}"
    done

    COUNTEREXAMPLES_DIR="${SPEC_ROOT}/examples/invalid"
    for COUNTEREXAMPLE in $(ls "${COUNTEREXAMPLES_DIR}"/*-0*.yaml) ; do
        ${RUN} linkml validate \
            --schema "${SPEC_ROOT}/${SCHEMA_FILE}" \
            --target-class "${TARGET_CLASS}" \
            "${COUNTEREXAMPLE}" \
                && echo "ERROR: Validation of 'examples/invalid/${COUNTEREXAMPLE}' was expected to fail, but has succeeded." \
                || echo "ok: validation failed, as expected"
    done

    # does not work due to following LinkML bugs:
    # https://github.com/linkml/linkml/issues/2423
    # https://github.com/linkml/linkml/issues/2425
    if false ; then
    ${RUN} linkml examples \
        --schema "${SPEC_ROOT}/*.linkml.yaml" \
        --input-directory "${SPEC_ROOT}/examples/valid" \
        --counter-example-input-directory "${SPEC_ROOT}/examples/invalid" \
        --output-directory "${SPEC_ROOT}/output"
    fi
}

for spec in $(ls "${CONFIGS}") ; do
    gen_spec "${spec}"
done

