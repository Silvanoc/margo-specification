#!/usr/bin/env bash

set -eu

THIS_SCRIPT="$(readlink -f "${0}")"
THIS_DIR="$(dirname "${THIS_SCRIPT}")"

ROOT_DIR="$(dirname "$(dirname "${THIS_DIR}")")"

TGT_DIR="${ROOT_DIR}/generated/openapi"
TGT_FILE="${TGT_DIR}/workload-management-api-1.0.0.openapi.yaml"

# Tracked location in system-design/ — this is what mkdocs and the repo use
SYSTEM_DESIGN_FILE="${ROOT_DIR}/system-design/specification/margo-management-interface/workload-management-api-1.0.0.yaml"

if command -v poetry &>/dev/null; then
  RUN="poetry run"
else
  if ! command -v linkml &>/dev/null; then
    echo "The command 'linkml' is missing"
    exit 1
  fi
  RUN=""
fi

mkdir -p "${TGT_DIR}"

# TODO: remove following block after LinkML release >v1.11.1
(
  cd data-model/tools
  poetry run python openapigen.py --keep-unreferenced --inline-enums -t workload-management-api-1.0.0.openapi.yaml ../margo-data-model.linkml.yaml \
    >"${TGT_FILE}"
  cp "${TGT_FILE}" "${SYSTEM_DESIGN_FILE}"
)
exit

${RUN} linkml generate openapi \
  --template "${THIS_DIR}/workload-management-api-1.0.0.openapi.yaml" \
  --inline-enums \
  --keep-unreferenced \
  "${ROOT_DIR}/data-model/margo-data-model.linkml.yaml" \
  >"${TGT_FILE}"

# Copy to the tracked location in system-design/ so it is picked up by
# generate-docs.bash (which copies system-design/ → merged/) and by git
cp "${TGT_FILE}" "${SYSTEM_DESIGN_FILE}"
