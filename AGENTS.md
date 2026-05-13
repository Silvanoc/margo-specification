# AGENTS.md — Margo Specification Contributor Guide

## Project Overview

The Margo Specification defines open standards for workload fleet management on edge compute devices. This repository contains the normative specification documents, some authored manually in MarkDown and others generated from a [LinkML](https://linkml.io/) data model using Jinja2 templates.

The final HTML documentation is built with [MkDocs](https://www.mkdocs.org/) using the [Material theme](https://squidfunk.github.io/mkdocs-material/).

## Repository Layout

```
.
├── src/specification/                    # Legacy per-resource LinkML schemas + Jinja2 templates + examples
│   ├── applications/
│   │   ├── application-description.linkml.yaml
│   │   └── resources/
│   │       ├── class.md.jinja2
│   │       ├── index.md.jinja2
│   │       └── examples/{valid,invalid}/
│   └── margo-management-interface/
│       ├── desired-state.linkml.yaml
│       └── resources/
│           ├── index.md.jinja2
│           └── examples/{valid,invalid}/
├── data-model/                           # Aggregate data model (current source of truth)
│   ├── margo-data-model.linkml.yaml      # Top-level schema aggregating all sub-schemas
│   ├── application-description.linkml.yaml
│   ├── application-deployment.linkml.yaml
│   ├── desired-state-manifest.linkml.yaml
│   ├── device-capabilities.linkml.yaml
│   ├── deployment-status.linkml.yaml
│   ├── margo-resources.linkml.yaml
│   ├── margo-deployments.linkml.yaml
│   ├── tools/                            # Generation & validation scripts
│   │   ├── generate-all.bash             # Runs all generators in sequence
│   │   ├── generate-docs.bash            # Generates MarkDown from LinkML
│   │   ├── generate-json-schemas.bash    # Generates JSON-Schema artifacts
│   │   ├── generate-openapi.bash         # Generates OpenAPI spec
│   │   ├── generate-class-diagram.bash   # Generates PlantUML class diagrams
│   │   ├── check-examples.bash           # Validates schemas and examples
│   │   └── configurations/              # Per-spec JSON configs
│   │       ├── application-deployment.json
│   │       ├── application-description.json
│   │       ├── deployment-status.json
│   │       ├── desired-state-manifest.json
│   │       └── device-capabilities.json
│   ├── generation-gap.md                   # Differences between pre-draft and generated OpenAPI spec
│   └── resources/
│       ├── examples/{valid,invalid}/     # Valid and invalid example files
│       ├── markdown-templates/           # Templates for the aggregate data-model docs
│       └── markdown-templates_main-classes/ # Templates for per-resource docs
├── doc-generation/                       # Legacy scripts (superseded by data-model/tools/)
├── system-design/                        # Manually-authored + generated MarkDown (copied into merged/ by generate-docs.bash)
│   └── specification/                    # ← generated .md files land here
├── generated/                            # Additional generated artifacts (diagrams, OpenAPI, JSON-Schema, etc.)
├── merged/                               # Merged MarkDown tree used by mkdocs build
├── mkdocs.yml                            # MkDocs configuration
└── pyproject.toml                        # Python dependencies (linkml>=1.11.0, mkdocs, etc.)
```

## Setup

### Option A: Development Container

The repository includes a dev-container with all dependencies pre-installed. Open the repo in VS Code and accept the dev-container prompt.

### Option B: Poetry (recommended for local development)

```bash
poetry install
```

### Option C: pip

```bash
pip install ./pyproject.toml
```

## Key Commands

### Validate LinkML schemas and examples

```bash
data-model/tools/check-examples.bash
```

This script:
- Reads each config from `data-model/tools/configurations/*.json`
- Validates the corresponding LinkML schema
- Validates valid examples in `data-model/resources/examples/valid/` against the schema
- Validates that invalid examples in `data-model/resources/examples/invalid/` are correctly rejected
- Exits non-zero if any check fails

### Generate all artifacts

```bash
data-model/tools/generate-all.bash
```

This runs all generators in sequence: class diagrams, JSON-Schemas, OpenAPI, and MarkDown docs.

### Generate MarkDown from LinkML

```bash
data-model/tools/generate-docs.bash
```

This script:
- Generates per-resource MarkDown using `data-model/resources/markdown-templates_main-classes/`
- Generates the full data model MarkDown using `data-model/resources/markdown-templates/`
- Copies generated diagrams and OpenAPI spec into the merged tree
- Copies everything from `system-design/` and `generated/` into `merged/` (which is what `mkdocs build` reads)

### Generate JSON-Schemas

```bash
data-model/tools/generate-json-schemas.bash
```

Generates one `.schema.json` file per resource schema into `generated/json-schemas/`.

### Generate OpenAPI spec

```bash
data-model/tools/generate-openapi.bash
```

Generates `workload-management-api-1.0.0.openapi.yaml` into `generated/openapi/`.

### Generate class diagrams

```bash
data-model/tools/generate-class-diagram.bash
```

Generates SVG/PNG class diagrams via PlantUML into `generated/diagrams/`.

### Build HTML documentation

```bash
mkdocs build          # one-time build
mkdocs serve          # live-reloading local server
```

## Generation Pipeline

Understanding how artifacts flow through the pipeline is essential when modifying schemas or templates.

### Artifact flow

```
data-model/*.linkml.yaml          (source of truth — LinkML schemas)
         │
         ├──► data-model/tools/check-examples.bash
         │       uses: data-model/tools/configurations/*.json
         │       validates: data-model/resources/examples/{valid,invalid}/
         │
         ├──► data-model/tools/generate-docs.bash   (orchestrator)
         │       │
         │       ├──► linkml generate doc  (per-resource, using markdown-templates_main-classes/)
         │       │       → generated/markdown_main-classes/<schema>.md
         │       │       → moved into merged/specification/{applications,margo-management-interface}/
         │       │
         │       ├──► linkml generate doc  (aggregate, using markdown-templates/)
         │       │       → generated/markdown/*
         │       │       → moved into merged/data-model/
         │       │
         │       ├──► generate-class-diagram.bash
         │       │       → generated/diagrams/DataModel-ClassDiagram.{svg,png}
         │       │       → copied into merged/figures/
         │       │
         │       ├──► generate-openapi.bash
         │       │       → generated/openapi/workload-management-api-1.0.0.openapi.yaml
         │       │       → moved into merged/specification/margo-management-interface/
         │       │
         │       └──► JSON schemas copied into merged/json-schemas/
         │
         └──► data-model/tools/generate-json-schemas.bash   (standalone)
                 → generated/json-schemas/*.schema.json

mkdocs build  reads from merged/   →   site/
```

Key points:
- `mkdocs build` reads from `merged/`, not directly from `system-design/` or `generated/`. The `generate-docs.bash` script copies everything into `merged/` first.
- The per-resource Markdown generation and the aggregate data-model generation use **different template directories** and produce output in **different locations**.
- `check-examples.bash` reads the list of schemas from `data-model/tools/configurations/*.json`, but `generate-docs.bash` and `generate-json-schemas.bash` have **hardcoded** schema lists. When adding a new resource, you must update all three.

### OpenAPI generation

The OpenAPI spec is generated by `data-model/tools/openapigen.py`, which:
- Reads an OpenAPI template (`data-model/tools/workload-management-api-1.0.0.openapi.yaml`) that defines endpoints, security schemes, and request/response structure.
- Fills in `components/schemas` from the LinkML model using the JSON-Schema generator.
- Only classes referenced by the endpoints in the template are included in the output.

When adding a new resource to the API, you must update both the LinkML schema **and** the OpenAPI template (add new endpoints that reference the new class). The template follows standard OpenAPI 3.0.3 structure — add a new entry under `paths` with request/response schemas that use `$ref: "#/components/schemas/<ClassName>"`.

## Legacy Code

The `src/specification/` directory contains the original per-resource LinkML schemas, templates, and examples. These are **legacy** and no longer the source of truth. The current source of truth is `data-model/`. Do not modify files under `src/specification/` unless specifically instructed.

The `doc-generation/` directory contains the original generation and validation scripts. These have been superseded by `data-model/tools/`. Do not use the old scripts.

## How to Modify the LinkML Data Model

### Step 1: Edit the schema

The **source of truth** for LinkML-specified resources lives under `data-model/`. Each resource has its own `.linkml.yaml` file. The aggregate schema `data-model/margo-data-model.linkml.yaml` imports all sub-schemas.

When making changes:

1. Edit the relevant `.linkml.yaml` file to add/modify classes, attributes, enums, slots, or types.
2. Add or update valid examples in `data-model/resources/examples/valid/` to cover the new or changed model elements.
3. Add invalid counter-examples in `data-model/resources/examples/invalid/` if new validation rules are introduced.
4. If the change affects rendering, update the Jinja2 templates:
   - `data-model/resources/markdown-templates_main-classes/` — for per-resource specification pages (attribute tables, examples, JSON-Schema links).
   - `data-model/resources/markdown-templates/` — for the aggregate data-model documentation (class hierarchy, diagrams).
5. If the change adds new API endpoints, update the OpenAPI template `data-model/tools/workload-management-api-1.0.0.openapi.yaml`.

### Step 2: Validate

```bash
data-model/tools/check-examples.bash
```

Fix any validation errors before proceeding.

### Step 3: Regenerate artifacts

```bash
data-model/tools/generate-all.bash
```

This runs all generators in sequence. Alternatively, run individual generators if you only need to update one artifact type.

The generated `.md` files land under `system-design/specification/` and `system-design/data-model/`. Generated JSON-Schemas, OpenAPI specs, and diagrams land under `generated/`. Verify the output looks correct.

### Step 4: Preview the site

```bash
mkdocs serve
```

Open http://127.0.0.1:8000 and navigate to the relevant specification page to visually verify.

### Step 5: Commit

Include the modified LinkML schema, updated examples, and all regenerated artifacts (`system-design/`, `generated/`) in your commit. These directories are tracked in git and must reflect the generated output.

## Adding a New LinkML-Specified Resource

1. Add the LinkML schema: `data-model/<resource-name>.linkml.yaml`.
2. Add valid examples: `data-model/resources/examples/valid/<TargetClass>-NNN.{yaml,json}`.
3. Add invalid counter-examples: `data-model/resources/examples/invalid/<TargetClass>-NNN.{yaml,json}`.
4. Add a configuration file in `data-model/tools/configurations/<resource-name>.json` with:
   ```json
   {
       "root": "data-model",
       "targetclass": "<RootClassName>",
       "schemafile": "<resource-name>.linkml.yaml",
       "markdowndoc": "<output-filename>.md"
   }
   ```
5. Add an import in `data-model/margo-data-model.linkml.yaml`.
6. Add the new MarkDown file to `mkdocs.yml` under the `nav` section.
7. Add the schema name to the hardcoded lists in `generate-docs.bash` (line 41) and `generate-json-schemas.bash` (line 24).
8. Run validation and generation as described above.

## Jinja2 Templates

The generation uses `linkml generate doc`, which provides the following variables and objects in the template context:

- `schema` — the parsed LinkML schema object
- `schemaview` — a `SchemaView` instance for querying classes, slots, enums, etc.
- `gen` — the generator instance with helper methods like `all_class_objects()`, `get_direct_slots()`, `link()`, `mermaid_diagram()`

Common patterns in existing templates:

- Iterate over class slots: `{% for slot in schemaview.class_slots("ClassName")|sort(attribute='rank') %}`
- Get slot details: `schemaview.get_slot(slot_name).range`, `.required`, `.description`
- Include example files: `{% include 'examples/valid/FileName.yaml' %}`
- Format ranges with inline macros for multivalued/inlined slots (see `index.md.jinja2` in each template directory)

There are two separate sets of templates that serve different purposes:

| Template directory | Used by | Produces | Output location |
| --- | --- | --- | --- |
| `data-model/resources/markdown-templates_main-classes/` | `generate-docs.bash` (per-resource loop) | One `.md` per schema with attribute tables, examples, JSON-Schema links | `merged/specification/{applications,margo-management-interface}/` |
| `data-model/resources/markdown-templates/` | `generate-docs.bash` (aggregate step) | Full data model overview with class hierarchy, diagrams, all-class listing | `merged/data-model/` |

Each directory contains an `index.md.jinja2` (the main page) and may contain `class.md.jinja2` (individual class detail pages). When modifying rendering, determine which template directory to edit based on the table above.

**When do templates need updating?** Most schema changes (adding/removing attributes, changing types, adding enums) do **not** require template changes — the templates iterate dynamically over class slots. Templates need updating only when:
- Changing the **structure** of the rendered page (e.g., adding a new section, changing table columns)
- Changing how **multivalued/inlined ranges** are displayed (the `format_range` macro in `index.md.jinja2`)
- Adding support for a **new example format** (e.g., rendering `.json` examples alongside `.yaml`)

## CI

The GitHub Actions pipeline (`.github/workflows/pages.yml`) runs:

1. **Quality checks** — validates `pyproject.toml` and `poetry.lock` consistency
2. **Validation** — runs `data-model/tools/check-examples.bash`
3. **Document generation** — runs `data-model/tools/generate-docs.bash`
4. **Pages build & deploy** — deploys to GitHub Pages on the `pre-draft` branch

PR checks (`.github/workflows/pr-checks.yml`) verify that commits are signed off.

## Conventions

- Sign off all commits (`git commit -s`)
- All contributions require CLA compliance (EasyCLA)
- One logical change per commit; the tree must build and work after each commit
- Base PRs on the `pre-draft` branch
- Example files follow the naming convention `<TargetClass>-NNN.{yaml,json}` (e.g., `ApplicationDescription-001.yaml`, `DeploymentStatusManifest-001.json`)
- LinkML schemas use the `.linkml.yaml` extension
- The YAML language server schema annotation `# yaml-language-server: $schema=...` should be kept at the top of each schema file for IDE support
- Do **not** add `default_range: string` to schemas that define slots using `any_of` — it causes the JSON-Schema generator to emit `type: string` at the top level, overriding the `anyOf` union. See [linkml/linkml#1483](https://github.com/linkml/linkml/issues/1483)
- Omit explicit `required: false` on optional attributes — the LinkML default is already `false`
