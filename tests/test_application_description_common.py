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
        self.assertIn("Parameter", classes)
        self.assertTrue(classes["ApplicationDescription"].tree_root)
        for name in ("key", "components", "id"):
            self.assertTrue(view.induced_slot(name, "DeploymentProfile").required)
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

    def test_optional_oci_import_and_induced_slots(self):
        schema = Path(__file__).resolve().parents[1] / "model/oci-component-properties.linkml.yaml"
        view = SchemaView(str(schema))
        self.assertIn("ComponentProperties", view.all_classes())
        self.assertEqual(view.get_class("OCIComponentProperties").is_a, "ComponentProperties")
        self.assertFalse(view.get_class("OCIComponentProperties").extra_slots.allowed)
        for name in ("repository", "revision"):
            self.assertTrue(view.induced_slot(name, "OCIComponentProperties").required)

    def test_induced_common_constraints(self):
        schema = Path(__file__).resolve().parents[1] / "model/application-description.linkml.yaml"
        view = SchemaView(str(schema))
        profiles = view.induced_slot("deploymentProfiles", "ApplicationDescription")
        self.assertEqual(profiles.range, "DeploymentProfile")
        self.assertTrue(profiles.required and profiles.multivalued and profiles.inlined_as_list)
        key = view.induced_slot("key", "DeploymentProfile")
        self.assertTrue(key.required)
        self.assertEqual(key.range, "string")
        self.assertIsNone(key.equals_string)
        self.assertEqual(key.pattern, r"\S")
        components = view.induced_slot("components", "DeploymentProfile")
        self.assertTrue(components.required and components.multivalued and components.inlined_as_list)
        self.assertEqual(components.range, "Component")
        self.assertTrue(view.get_class("ComponentProperties").extra_slots.allowed)
        self.assertTrue(view.induced_slot("pointer", "ParameterTarget").required)
        self.assertTrue(view.induced_slot("components", "ParameterTarget").required)
        self.assertTrue(view.get_class("ParameterTarget").extra_slots.allowed)
        self.assertEqual(len(view.get_class("MatchExpression").rules), 16)
