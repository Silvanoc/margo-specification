

# Slot: targets 


_Used to indicate which component the value should be applied to when installing, or updating, the application.  See the [Target](#target-attributes) section below._





URI: [https://specification.margo.org/data-model/targets](https://specification.margo.org/data-model/targets)
Alias: targets

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Parameter](Parameter.md) | Defines a configurable parameter for the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Target](Target.md) |
| Domain Of | [Parameter](Parameter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Parameter](Parameter.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/targets |
| native | https://specification.margo.org/data-model/targets |




## LinkML Source

<details>
```yaml
name: targets
description: Used to indicate which component the value should be applied to when
  installing, or updating, the application.  See the [Target](#target-attributes)
  section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: targets
owner: Parameter
domain_of:
- Parameter
range: Target
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>