

# Slot: serialNumber 


_Defines the serial number of the device._





URI: [https://specification.margo.org/data-model/serialNumber](https://specification.margo.org/data-model/serialNumber)
Alias: serialNumber

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
| self | https://specification.margo.org/data-model/serialNumber |
| native | https://specification.margo.org/data-model/serialNumber |




## LinkML Source

<details>
```yaml
name: serialNumber
description: Defines the serial number of the device.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: serialNumber
owner: Properties
domain_of:
- Properties
range: string
required: true

```
</details>