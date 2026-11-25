"""The workload target characteristic subschema stands alone and is reusable."""

import re
import tempfile
import unittest
from pathlib import Path

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
            "OtherCharacteristic", "OtherCharacteristicProperties",
        })
        self.assertFalse(any(c.tree_root for c in classes.values()))
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
