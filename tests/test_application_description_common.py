"""The shared application subschema must stand alone."""

import unittest
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView


class CommonSchemaTests(unittest.TestCase):
    def test_induced_ranges_resolve_without_a_deployment_schema(self):
        schema = (
            Path(__file__).resolve().parents[1]
            / "model"
            / "application-description.linkml.yaml"
        )
        view = SchemaView(str(schema))
        classes = view.all_classes(imports=False)
        self.assertNotIn("Parameter", classes)
        ranges = set(view.all_classes()) | set(view.all_types()) | set(view.all_enums())
        for name in classes:
            for slot in view.class_induced_slots(name):
                for range_name in [slot.range] + [
                    item.range for item in slot.any_of or []
                ]:
                    if range_name:
                        with self.subTest(
                            class_name=name, slot=slot.name, range=range_name
                        ):
                            self.assertIn(range_name, ranges)
