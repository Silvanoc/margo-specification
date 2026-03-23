

# Slot: model 


_The model of the peripheral. If `model` is specified as a requirement here, it may be difficult to find devices that can host the application. Please use these requirements with caution._





URI: [https://specification.margo.org/data-model/model](https://specification.margo.org/data-model/model)
Alias: model

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

**Rank:** 40






### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/model |
| native | https://specification.margo.org/data-model/model |




## LinkML Source

<details>
```yaml
name: model
description: The model of the peripheral. If `model` is specified as a requirement
  here, it may be difficult to find devices that can host the application. Please
  use these requirements with caution.
from_schema: https://specification.margo.org/data-model
rank: 40
alias: model
owner: Peripheral
domain_of:
- Peripheral
range: string
required: false

```
</details>