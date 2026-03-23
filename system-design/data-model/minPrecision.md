

# Slot: minPrecision 


_If set, indicates the minimum level of precision the value must have to be considered valid._





URI: [https://specification.margo.org/data-model/minPrecision](https://specification.margo.org/data-model/minPrecision)
Alias: minPrecision

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NumericDoubleValidationSchema](NumericDoubleValidationSchema.md) | Extends schema to define a double-specific set of validation rules that can b... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](integer.md) |
| Domain Of | [NumericDoubleValidationSchema](NumericDoubleValidationSchema.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [NumericDoubleValidationSchema](NumericDoubleValidationSchema.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/minPrecision |
| native | https://specification.margo.org/data-model/minPrecision |




## LinkML Source

<details>
```yaml
name: minPrecision
description: If set, indicates the minimum level of precision the value must have
  to be considered valid.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: minPrecision
owner: NumericDoubleValidationSchema
domain_of:
- NumericDoubleValidationSchema
range: integer
required: false

```
</details>