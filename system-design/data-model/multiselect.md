

# Slot: multiselect 


_If true, indicates multiple values can be selected. If multiple values can be selected the resulting value is an array of the selected values. The default is false if not provided._





URI: [https://specification.margo.org/data-model/multiselect](https://specification.margo.org/data-model/multiselect)
Alias: multiselect

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SelectValidationSchema](SelectValidationSchema.md) | Extends schema to define a specific set of validation rules that can be used ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [boolean](boolean.md) |
| Domain Of | [SelectValidationSchema](SelectValidationSchema.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | https://specification.margo.org/data-model/multiselect |
| native | https://specification.margo.org/data-model/multiselect |




## LinkML Source

<details>
```yaml
name: multiselect
description: If true, indicates multiple values can be selected. If multiple values
  can be selected the resulting value is an array of the selected values. The default
  is false if not provided.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: multiselect
owner: SelectValidationSchema
domain_of:
- SelectValidationSchema
range: boolean
required: false

```
</details>