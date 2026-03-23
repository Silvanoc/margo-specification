

# Slot: parameter 


_The name of the [parameter](#parameter-attributes) the setting is associated with._





URI: [https://specification.margo.org/data-model/parameter](https://specification.margo.org/data-model/parameter)
Alias: parameter

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Setting](Setting.md) | Individual configuration settings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Setting](Setting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Setting](Setting.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/parameter |
| native | https://specification.margo.org/data-model/parameter |




## LinkML Source

<details>
```yaml
name: parameter
description: The name of the [parameter](#parameter-attributes) the setting is associated
  with.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: parameter
owner: Setting
domain_of:
- Setting
range: string
required: true

```
</details>