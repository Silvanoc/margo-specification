

# Slot: name 



URI: [https://specification.margo.org/data-model/name](https://specification.margo.org/data-model/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeploymentMetadata](DeploymentMetadata.md) | Metadata associated with the desired state |  no  |
| [TextValidationSchema](TextValidationSchema.md) | Extends schema to define a string/text-specific set of validation rules that ... |  no  |
| [Parameter](Parameter.md) | Defines a configurable parameter for the application |  no  |
| [Schema](Schema.md) | Defines data type and rules for validating user provided parameter values |  no  |
| [Setting](Setting.md) | Individual configuration settings |  no  |
| [NumericIntegerValidationSchema](NumericIntegerValidationSchema.md) | Extends schema to define a integer-specific set of validation rules that can ... |  no  |
| [ApplicationMetadata](ApplicationMetadata.md) | Metadata about the application |  no  |
| [BooleanValidationSchema](BooleanValidationSchema.md) | Extends schema to define a boolean-specific set of validation rules that can ... |  no  |
| [NumericDoubleValidationSchema](NumericDoubleValidationSchema.md) | Extends schema to define a double-specific set of validation rules that can b... |  no  |
| [SelectValidationSchema](SelectValidationSchema.md) | Extends schema to define a specific set of validation rules that can be used ... |  no  |
| [Section](Section.md) | Named sections within the configuration layout |  no  |
| [Component](Component.md) | A class representing a component of a deployment profile |  no  |
| [Author](Author.md) | Information about the application's author |  no  |
| [ComponentStatus](ComponentStatus.md) | Status of a component deployment |  no  |
| [ComposeComponent](ComposeComponent.md) |  |  no  |
| [Organization](Organization.md) | Information about the providing organization |  no  |
| [HelmComponent](HelmComponent.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE |
| Domain Of | [Component](Component.md), [Parameter](Parameter.md), [DeploymentMetadata](DeploymentMetadata.md), [ApplicationMetadata](ApplicationMetadata.md), [Author](Author.md), [Organization](Organization.md), [Section](Section.md), [Setting](Setting.md), [Schema](Schema.md), [ComponentStatus](ComponentStatus.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/name |
| native | https://specification.margo.org/data-model/name |




## LinkML Source

<details>
```yaml
name: name
alias: name
domain_of:
- Component
- Parameter
- DeploymentMetadata
- ApplicationMetadata
- Author
- Organization
- Section
- Setting
- Schema
- ComponentStatus

```
</details>