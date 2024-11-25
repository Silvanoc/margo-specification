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
    echo "${SPEC_ROOT}"

    EXAMPLES_DIR="${SPEC_ROOT}/examples/valid"
    for EXAMPLE in $(ls "${EXAMPLES_DIR}"/DesiredState-0*.yaml) ; do
         ${RUN} linkml validate \
            --schema "${SPEC_ROOT}/desired-state.linkml.yaml" \
            --target-class DesiredState \
            "${EXAMPLE}"
    done

    COUNTEREXAMPLES_DIR="${SPEC_ROOT}/examples/invalid"
    for COUNTEREXAMPLE in $(ls "${COUNTEREXAMPLES_DIR}"/DesiredState-0*.yaml) ; do
        ${RUN} linkml validate \
            --schema "${SPEC_ROOT}/desired-state.linkml.yaml" \
            --target-class DesiredState \
            "${COUNTEREXAMPLE}" \
                && echo "ERROR: Validation of 'examples/invalid/${COUNTEREXAMPLE}' was expected to fail, but has succeeded." \
                || echo "ok: validation failed, as expected"
    done

    # does not work due to following LinkML bugs:
    # https://github.com/linkml/linkml/issues/2423
    # https://github.com/linkml/linkml/issues/2425
    if false ; then
    ${RUN} linkml examples \
        --schema "${SPEC_ROOT}/desired-state.linkml.yaml" \
        --input-directory "${SPEC_ROOT}/examples/valid" \
        --counter-example-input-directory "${SPEC_ROOT}/examples/invalid" \
        --output-directory "${SPEC_ROOT}/output"
    fi
}

for spec in $(ls "${CONFIGS}") ; do
    gen_spec "${spec}"
done

