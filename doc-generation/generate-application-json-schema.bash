#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="${ROOT_DIR}/build/json-schema"
mkdir -p "${OUTPUT_DIR}"
TEMP_FILE="$(mktemp "${OUTPUT_DIR}/.application-description.XXXXXX")"
trap 'rm -f "${TEMP_FILE}"' EXIT
linkml generate json-schema --top-class ApplicationDescription \
    --include-range-class-descendants --preserve-names \
    "${ROOT_DIR}/src/specification/applications/application-description.linkml.yaml" > "${TEMP_FILE}"
mv "${TEMP_FILE}" "${OUTPUT_DIR}/application-description.schema.json"
echo "Generated ${OUTPUT_DIR}/application-description.schema.json"
