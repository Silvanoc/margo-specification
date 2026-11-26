#!/usr/bin/env python3
"""Check valid and invalid application examples against a generated JSON Schema."""

import argparse
import json
from pathlib import Path
import sys

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA = ROOT / "build/json-schema/application-description.schema.json"
DEFAULT_EXAMPLES = ROOT / "tests/fixtures/generic-application"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--examples", type=Path, default=DEFAULT_EXAMPLES,
                        help="directory containing valid/ and invalid/ fixtures")
    args = parser.parse_args()
    try:
        with args.schema.open(encoding="utf-8") as stream:
            schema = json.load(stream)
        if not isinstance(schema, (dict, bool)):
            raise ValueError("JSON Schema must be an object or boolean")
        validator_class = jsonschema.validators.validator_for(schema)
        validator_class.check_schema(schema)
        validator = validator_class(schema)
        failed = False
        for category in ("valid", "invalid"):
            directory = args.examples / category
            if not directory.is_dir():
                raise ValueError(f"missing examples directory: {directory}")
            fixtures = sorted(p for p in directory.iterdir()
                              if p.is_file() and p.suffix.lower() in (".yaml", ".yml", ".json"))
            if not fixtures:
                raise ValueError(f"no YAML or JSON fixtures in {directory}")
            for fixture in fixtures:
                try:
                    with fixture.open(encoding="utf-8") as stream:
                        instance = json.load(stream) if fixture.suffix.lower() == ".json" else yaml.safe_load(stream)
                except (OSError, ValueError, yaml.YAMLError) as error:
                    raise ValueError(f"cannot parse {fixture}: {error}") from error
                errors = list(validator.iter_errors(instance))
                expected = category == "invalid"
                if bool(errors) != expected:
                    failed = True
                    print(f"FAIL {fixture}: " + ("unexpected validation errors" if errors else "expected validation errors"), file=sys.stderr)
                else:
                    print(f"OK {fixture}: " + ("invalid as expected" if errors else "valid"))
                for error in errors:
                    path = "/" + "/".join(str(part) for part in error.absolute_path)
                    print(f"  {path}: {error.message}")
        return int(failed)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
