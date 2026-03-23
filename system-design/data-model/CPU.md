

# Slot: cpu 


_CPU element specifying the CPU requirements for the application. See the [CPU](#cpu-attributes) section below._





URI: [https://specification.margo.org/data-model/cpu](https://specification.margo.org/data-model/cpu)
Alias: cpu

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resources](Resources.md) | Required resources element specifying the resources required to install the a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CPU](CPU.md) |
| Domain Of | [Resources](Resources.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/cpu |
| native | https://specification.margo.org/data-model/cpu |




## LinkML Source

<details>
```yaml
name: cpu
description: CPU element specifying the CPU requirements for the application. See
  the [CPU](#cpu-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: cpu
domain_of:
- Resources
range: CPU
required: false

```
</details>