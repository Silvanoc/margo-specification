#!/usr/bin/env bash

set -eu

THIS_SCRIPT="$(readlink -f "${0}")"
THIS_DIR="$(dirname "${THIS_SCRIPT}")"
ROOT_DIR="$(dirname "${THIS_DIR}")"
RUN="poetry -C "${THIS_DIR}" run"
DOCS_GEN="${THIS_DIR}"
CONFIGS="${DOCS_GEN}/configurations"

gen_spec () {
    ITEM_REL_PATH=$(jq -r '.root' "${CONFIGS}/$1")
    SCHEMA_FILE=$(jq -r '.schemafile' "${CONFIGS}/$1")
    MKDOWN_FILE=$(jq -r '.markdowndoc' "${CONFIGS}/$1")
    SRC_ROOT="${ROOT_DIR}/${ITEM_REL_PATH}"
    SPEC_ROOT="${ROOT_DIR}/system-design${ITEM_REL_PATH#src}"
    echo "${SRC_ROOT}"

    ${RUN} linkml generate doc \
        --directory="${SRC_ROOT}/docs" \
        --template-directory="${SRC_ROOT}/resources" \
        "${SRC_ROOT}/${SCHEMA_FILE}"

    mv "${SRC_ROOT}/docs/index.md" "${SPEC_ROOT}/${MKDOWN_FILE}"
    rm -r "${SRC_ROOT}/docs"
}

for spec in $(ls "${CONFIGS}") ; do
    gen_spec "${spec}"
done

${RUN} mkdocs build
