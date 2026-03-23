

# Slot: regexMatch 


_If set, indicates a regular expression to use to validate the value._





URI: [https://specification.margo.org/data-model/regexMatch](https://specification.margo.org/data-model/regexMatch)
Alias: regexMatch

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextValidationSchema](TextValidationSchema.md) | Extends schema to define a string/text-specific set of validation rules that ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
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
| self | https://specification.margo.org/data-model/regexMatch |
| native | https://specification.margo.org/data-model/regexMatch |




## LinkML Source

<details>
```yaml
name: regexMatch
description: If set, indicates a regular expression to use to validate the value.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: regexMatch
owner: TextValidationSchema
domain_of:
- TextValidationSchema
range: string
required: false

```
</details>