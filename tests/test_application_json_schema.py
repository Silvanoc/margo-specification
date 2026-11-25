"""Focused checks of the generic application JSON Schema tools."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
GENERATOR = ROOT / "doc-generation/generate-application-json-schema.bash"
CHECKER = ROOT / "doc-generation/validate-application-json-schema.py"
SCHEMA = ROOT / "build/json-schema/application-description.schema.json"


def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


class ApplicationJsonSchemaTests(unittest.TestCase):
    def test_generation_and_repository_examples(self):
        env = os.environ.copy()
        env["PATH"] = str(Path(sys.executable).parent) + os.pathsep + env.get("PATH", "")
        result = subprocess.run(["bash", str(GENERATOR)], cwd=ROOT, text=True,
                                capture_output=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        schema = json.loads(SCHEMA.read_text())
        self.assertIn("ApplicationDescription", schema["$defs"])
        result = run(sys.executable, str(CHECKER))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        custom = ROOT / "tests/fixtures/generic-application/valid/mixed.yaml"
        instance = yaml.safe_load(custom.read_text())
        profiles = instance["deploymentProfiles"]
        self.assertEqual([p["key"] for p in profiles], [
            "margo.org/deployment/helm", "margo.org/deployment/compose",
            "margo.org/deployment/helm", "example.org/deployment/future"])
        validator = jsonschema.validators.validator_for(schema)(schema)
        self.assertEqual(list(validator.iter_errors(instance)), [])
        self.assertNotIn("repository", profiles[-1]["components"][0]["properties"])
        target = instance["parameters"]["greeting"]["targets"][0]
        self.assertEqual(target["futureTargetField"], {"nested": [1, True]})
        for field in ("pointer", "components"):
            with self.subTest(missing_target_field=field):
                value = target.pop(field)
                self.assertTrue(list(validator.iter_errors(instance)))
                target[field] = value
        for key in ("", "  \t\n"):
            with self.subTest(key=key):
                profiles[-1]["key"] = key
                self.assertTrue(list(validator.iter_errors(instance)))
        profiles[-1]["key"] = "arbitrary/unknown-deployment"
        self.assertEqual(list(validator.iter_errors(instance)), [])
        examples = ROOT / "tests/fixtures/generic-application/invalid"
        for name in ("missing-key.yaml", "missing-components.yaml", "missing-id.yaml"):
            with self.subTest(fixture=name):
                instance = yaml.safe_load((examples / name).read_text())
                errors = list(validator.iter_errors(instance))
                self.assertEqual(len(errors), 1, [error.message for error in errors])

    def test_errors_and_expectations(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            examples = root / "examples"
            (examples / "valid").mkdir(parents=True)
            (examples / "invalid").mkdir()
            schema = root / "schema.json"
            schema.write_text(json.dumps({"type": "object", "required": ["id"]}))
            good = examples / "valid/good.json"
            bad = examples / "invalid/bad.yaml"
            good.write_text('{"id": "x"}')
            bad.write_text('{}')

            def check(path=schema):
                return run(sys.executable, str(CHECKER), "--schema", str(path),
                           "--examples", str(examples))

            self.assertEqual(check().returncode, 0)
            good.write_text('{}')
            self.assertEqual(check().returncode, 1)
            good.write_text('{"id": "x"}')
            bad.write_text('id: x')
            self.assertEqual(check().returncode, 1)
            bad.write_text('[')
            self.assertEqual(check().returncode, 2)
            bad.unlink()
            self.assertEqual(check().returncode, 2)
            self.assertEqual(check(root / "missing.json").returncode, 2)
            schema.write_text('{')
            self.assertEqual(check().returncode, 2)
            schema.write_text('{"type": "not-a-type"}')
            self.assertEqual(check().returncode, 2)


if __name__ == "__main__":
    unittest.main()
