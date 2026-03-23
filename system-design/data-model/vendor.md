

# Slot: vendor 


_Defines the device vendor._





URI: [https://specification.margo.org/data-model/vendor](https://specification.margo.org/data-model/vendor)
Alias: vendor

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Properties](Properties.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Properties](Properties.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Properties](Properties.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/vendor |
| native | https://specification.margo.org/data-model/vendor |




## LinkML Source

<details>
```yaml
name: vendor
description: Defines the device vendor.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: vendor
owner: Properties
domain_of:
- Properties
range: string
required: true

```
</details>