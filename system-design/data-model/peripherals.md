

# Slot: peripherals 


_Peripherals element specifying the peripherals required to run the application. See the [Peripheral](#peripheral-attributes) section below._





URI: [https://specification.margo.org/data-model/peripherals](https://specification.margo.org/data-model/peripherals)
Alias: peripherals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resources](Resources.md) | Required resources element specifying the resources required to install the a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Peripheral](Peripheral.md) |
| Domain Of | [Resources](Resources.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/peripherals |
| native | https://specification.margo.org/data-model/peripherals |




## LinkML Source

<details>
```yaml
name: peripherals
description: Peripherals element specifying the peripherals required to run the application.
  See the [Peripheral](#peripheral-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: peripherals
domain_of:
- Resources
range: Peripheral
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>