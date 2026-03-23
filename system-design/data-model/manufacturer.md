

# Slot: manufacturer 


_The name of the manufacturer. If `manufacturer` is specified as a requirement here, it may be difficult to find devices that can host the  application. Please use these requirements with caution._





URI: [https://specification.margo.org/data-model/manufacturer](https://specification.margo.org/data-model/manufacturer)
Alias: manufacturer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Peripheral](Peripheral.md) | Peripheral hardware of a device |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Peripheral](Peripheral.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Peripheral](Peripheral.md) |












## Identifier and Mapping Information
### Administrative Metadata

**Rank:** 30






### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/manufacturer |
| native | https://specification.margo.org/data-model/manufacturer |




## LinkML Source

<details>
```yaml
name: manufacturer
description: The name of the manufacturer. If `manufacturer` is specified as a requirement
  here, it may be difficult to find devices that can host the  application. Please
  use these requirements with caution.
from_schema: https://specification.margo.org/data-model
rank: 30
alias: manufacturer
owner: Peripheral
domain_of:
- Peripheral
range: string
required: false

```
</details>