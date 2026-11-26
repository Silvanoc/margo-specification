"""The workload target characteristic subschema stands alone and is reusable."""

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import jsonschema
from linkml_runtime.utils.schemaview import SchemaView


SCHEMA = Path(__file__).resolve().parents[1] / "model/workload-target-characteristics.linkml.yaml"


class WorkloadTargetCharacteristicsTests(unittest.TestCase):
    def test_shared_classes_and_induced_ranges(self):
        view = SchemaView(str(SCHEMA))
        classes = view.all_classes(imports=False)
        self.assertEqual(set(classes), {
            "CpuCharacteristic", "CpuProperties", "Cpu", "MemoryCharacteristic",
            "MemoryProperties", "StorageCharacteristic", "StorageProperties",
            "PeripheralsCharacteristic", "PeripheralsProperties", "Peripheral",
            "InterfacesCharacteristic", "InterfacesProperties", "Interface",
            "OtherCharacteristic", "OtherCharacteristicProperties", "WorkloadTargetProfile",
        })
        self.assertFalse(any(c.tree_root for c in classes.values()))
        for cls in classes.values():
            for annotation in ("margo_profile_example", "margo_profile_kind", "margo_profile_characteristic"):
                self.assertNotIn(annotation, cls.annotations, cls.name)
        ranges = set(view.all_classes()) | set(view.all_types()) | set(view.all_enums())
        for name in classes:
            for slot in view.class_induced_slots(name):
                for range_name in [slot.range] + [item.range for item in slot.any_of or []]:
                    if range_name:
                        with self.subTest(class_name=name, slot=slot.name):
                            self.assertIn(range_name, ranges)
        for cls, slot, enum, values in (
            ("Cpu", "architecture", "CpuArchitecture", {"amd64", "arm64", "arm"}),
            ("Peripheral", "type", "PeripheralType", {"gpu", "display", "camera", "microphone", "speaker"}),
            ("Interface", "type", "InterfaceType", {"ethernet", "wifi", "cellular", "bluetooth", "usb", "canbus", "rs232"}),
        ):
            self.assertEqual(view.induced_slot(slot, cls).range, enum)
            self.assertEqual(set(view.get_enum(enum).permissible_values), values)

    def test_generic_profile_slots_and_annotations(self):
        view = SchemaView(str(SCHEMA))
        profile = view.get_class("WorkloadTargetProfile")
        self.assertFalse(profile.tree_root)
        self.assertEqual(profile.annotations["margo_extensions_pattern"].value,
                         r'^x-[a-z][a-z0-9-]*-extensions(?![\s\S])')
        slot = view.induced_slot("characteristics", "WorkloadTargetProfile")
        self.assertTrue(slot.required and slot.multivalued and slot.inlined and slot.inlined_as_list)
        self.assertEqual(slot.annotations["margo_unique_by"].value, "key")
        self.assertNotIn("margo_required_characteristics", slot.annotations)
        self.assertEqual([item.range for item in slot.any_of], [
            "CpuCharacteristic", "MemoryCharacteristic", "StorageCharacteristic",
            "PeripheralsCharacteristic", "InterfacesCharacteristic", "OtherCharacteristic",
        ])

    def test_generated_profile_json_schema(self):
        generator = Path(sys.executable).parent / "gen-json-schema"
        result = subprocess.run(
            [str(generator), "--top-class", "WorkloadTargetProfile", str(SCHEMA)],
            text=True, capture_output=True, check=True,
        )
        schema = json.loads(result.stdout)
        validator = jsonschema.validators.validator_for(schema)(schema)
        valid = [
            {"characteristics": []},
            {"characteristics": [{"key": "margo.org/deployment/future", "properties": {"nested": [1, {"custom": True}]}, "extra": 1}]},
            {"characteristics": [{"key": "margo.org/resource/cpu", "properties": {"cpus": [{"cores": 2}]}}]},
        ]
        invalid = [
            {}, {"characteristics": None}, {"characteristics": {}},
            {"characteristics": [42]},
            {"characteristics": [{"key": "margo.org/deployment/future"}]},
            {"characteristics": [{"key": "margo.org/resource/cpu", "properties": {"cpus": [{"cores": "invalid"}]}}]},
        ]
        for instance in valid:
            with self.subTest(valid=instance):
                self.assertEqual(list(validator.iter_errors(instance)), [])
        for instance in invalid:
            with self.subTest(invalid=instance):
                self.assertTrue(list(validator.iter_errors(instance)))

    def test_catch_all_is_open_to_deployment_types(self):
        view = SchemaView(str(SCHEMA))
        pattern = view.induced_slot("key", "OtherCharacteristic").pattern
        for key in ("margo.org/deployment/compose", "margo.org/deployment/helm",
                    "margo.org/deployment/future", "vendor/custom", "margo.org/resource/cpu-extra"):
            self.assertIsNotNone(re.match(pattern, key), key)
        for key in ("margo.org/resource/cpu", "margo.org/resource/memory",
                    "margo.org/resource/storage", "margo.org/peripherals", "margo.org/interfaces"):
            self.assertIsNone(re.match(pattern, key), key)
        self.assertTrue(view.get_class("OtherCharacteristic").extra_slots.allowed)
        self.assertTrue(view.get_class("OtherCharacteristicProperties").extra_slots.allowed)
        self.assertTrue(view.induced_slot("properties", "OtherCharacteristic").required)

    def test_known_keys_use_exact_equality(self):
        view = SchemaView(str(SCHEMA))
        result = subprocess.run(
            [str(Path(sys.executable).parent / "gen-json-schema"),
             "--top-class", "WorkloadTargetProfile", str(SCHEMA)],
            text=True, capture_output=True, check=True,
        )
        schema = json.loads(result.stdout)
        for cls, key in (
            ("CpuCharacteristic", "margo.org/resource/cpu"),
            ("MemoryCharacteristic", "margo.org/resource/memory"),
            ("StorageCharacteristic", "margo.org/resource/storage"),
            ("PeripheralsCharacteristic", "margo.org/peripherals"),
            ("InterfacesCharacteristic", "margo.org/interfaces"),
        ):
            with self.subTest(class_name=cls):
                slot = view.induced_slot("key", cls)
                self.assertEqual(slot.equals_string, key)
                self.assertIsNone(slot.pattern)
                key_schema = schema["$defs"][cls]["properties"]["key"]
                self.assertEqual(key_schema["const"], key)
                self.assertNotIn("pattern", key_schema)
                validator = jsonschema.validators.validator_for(schema)(key_schema)
                self.assertTrue(validator.is_valid(key))
                for suffix in ("\n", "\r\n", "/other"):
                    self.assertFalse(validator.is_valid(key + suffix))

    def test_imported_specialization_can_constrain_key(self):
        with tempfile.TemporaryDirectory() as directory:
            schema = Path(directory) / "profile.yaml"
            schema.write_text(f"""\
id: https://example.org/profile
name: Profile
prefixes:
  linkml: https://w3id.org/linkml/
  example: https://example.org/
imports:
  - {SCHEMA.with_suffix('')}
default_prefix: example
classes:
  LocalOtherCharacteristic:
    is_a: OtherCharacteristic
    slot_usage:
      key:
        pattern: '^local-only$'
""")
            view = SchemaView(str(schema))
            self.assertIn("CpuCharacteristic", view.all_classes())
            self.assertEqual(view.induced_slot("key", "LocalOtherCharacteristic").pattern, "^local-only$")
            self.assertEqual(view.induced_slot("properties", "LocalOtherCharacteristic").range, "OtherCharacteristicProperties")


if __name__ == "__main__":
    unittest.main()
