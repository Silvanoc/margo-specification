

# Slot: dataType 


_Indicates the expected data type for the user provided value. Accepted values are string, integer, double, boolean, array[string], array[integer], array[double], array[boolean]. At a minimum, the provided parameter value MUST match the schema's data type if no other validation rules are provided._





URI: [https://specification.margo.org/data-model/dataType](https://specification.margo.org/data-model/dataType)
Alias: dataType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextValidationSchema](TextValidationSchema.md) | Extends schema to define a string/text-specific set of validation rules that ... |  no  |
| [Schema](Schema.md) | Defines data type and rules for validating user provided parameter values |  no  |
| [NumericIntegerValidationSchema](NumericIntegerValidationSchema.md) | Extends schema to define a integer-specific set of validation rules that can ... |  no  |
| [NumericDoubleValidationSchema](NumericDoubleValidationSchema.md) | Extends schema to define a double-specific set of validation rules that can b... |  no  |
| [BooleanValidationSchema](BooleanValidationSchema.md) | Extends schema to define a boolean-specific set of validation rules that can ... |  no  |
| [SelectValidationSchema](SelectValidationSchema.md) | Extends schema to define a specific set of validation rules that can be used ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Schema](Schema.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Schema](Schema.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/dataType |
| native | https://specification.margo.org/data-model/dataType |




## LinkML Source

<details>
```yaml
name: dataType
description: Indicates the expected data type for the user provided value. Accepted
  values are string, integer, double, boolean, array[string], array[integer], array[double],
  array[boolean]. At a minimum, the provided parameter value MUST match the schema's
  data type if no other validation rules are provided.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: dataType
owner: Schema
domain_of:
- Schema
range: string
required: true

```
</details>