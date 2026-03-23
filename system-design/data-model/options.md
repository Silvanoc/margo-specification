

# Slot: options 


_This provides the list of acceptable options the user can select from. The data type for each option must match the parameter setting’s data type._





URI: [https://specification.margo.org/data-model/options](https://specification.margo.org/data-model/options)
Alias: options

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SelectValidationSchema](SelectValidationSchema.md) | Extends schema to define a specific set of validation rules that can be used ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [SelectValidationSchema](SelectValidationSchema.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SelectValidationSchema](SelectValidationSchema.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/options |
| native | https://specification.margo.org/data-model/options |




## LinkML Source

<details>
```yaml
name: options
description: This provides the list of acceptable options the user can select from.
  The data type for each option must match the parameter setting’s data type.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: options
owner: SelectValidationSchema
domain_of:
- SelectValidationSchema
range: string
required: true
multivalued: true

```
</details>