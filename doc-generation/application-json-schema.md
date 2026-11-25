# Generic application JSON Schema

With the project's Poetry environment installed, from the repository root:

```bash
export PYSTOW_HOME="$PWD/.cache/pystow"
poetry run bash doc-generation/generate-application-json-schema.bash
poetry run python doc-generation/validate-application-json-schema.py
```

The first command generates `build/json-schema/application-description.schema.json`
from `model/application-description.linkml.yaml`, using
`ApplicationDescription` as the root. The second reads that schema and the YAML
and JSON files directly under `tests/fixtures/generic-application/valid/`
and `invalid/`. Both directories must contain fixtures. Valid examples must pass;
invalid examples must produce JSON Schema validation errors. Parse errors, a missing
or malformed schema, and missing fixtures are failures, not successful counterexamples.
Use `--schema PATH` and `--examples DIRECTORY` to check other inputs. Exit status 0
means all expectations were met, 1 means an expectation failed, and 2 means an input
or validation setup error occurred.

The generated schema mirrors the current generic LinkML model; it is not a standalone
Compose- or Helm-specific validator. Profiles can have repeated or unknown keys;
deployment-type and corresponding component-type constraints require a separate validator.
Descriptions and other normative, cross-reference, or semantic requirements may not
be represented as JSON Schema constraints. Passing these checks is not proof of full
specification conformance. The existing LinkML example checker is separate.

The existing documentation generator still uses
`src/specification/applications/application-description.linkml.yaml`, which has
the older `type`/`deviceConstraints` representation and has not been migrated
to this common `key`/`placementConstraints` model.

Run the focused regression tests with:

```bash
export PYSTOW_HOME="$PWD/.cache/pystow"
poetry run python -m unittest discover -s tests -p 'test_application_json_schema.py'
```
