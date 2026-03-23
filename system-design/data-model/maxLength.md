

# Slot: maxLength 


_If set, indicates the maximum number of characters the value must have to be considered valid._





URI: [https://specification.margo.org/data-model/maxLength](https://specification.margo.org/data-model/maxLength)
Alias: maxLength

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextValidationSchema](TextValidationSchema.md) | Extends schema to define a string/text-specific set of validation rules that ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](integer.md) |
| Domain Of | [TextValidationSchema](TextValidationSchema.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TextValidationSchema](TextValidationSchema.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/maxLength |
| native | https://specification.margo.org/data-model/maxLength |




## LinkML Source

<details>
```yaml
name: maxLength
description: If set, indicates the maximum number of characters the value must have
  to be considered valid.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: maxLength
owner: TextValidationSchema
domain_of:
- TextValidationSchema
range: integer
required: false

```
</details>