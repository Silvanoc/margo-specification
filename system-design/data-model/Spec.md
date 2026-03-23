

# Slot: spec 


_Spec element that defines deployment profile and parameters associated with the application deployment. See the [Spec Attributes](#spec-attributes) section below._





URI: [https://specification.margo.org/data-model/spec](https://specification.margo.org/data-model/spec)
Alias: spec

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ApplicationDeployment](ApplicationDeployment.md) | A class representing the desired state of an entity |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Spec](Spec.md) |
| Domain Of | [ApplicationDeployment](ApplicationDeployment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ApplicationDeployment](ApplicationDeployment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/spec |
| native | https://specification.margo.org/data-model/spec |




## LinkML Source

<details>
```yaml
name: spec
description: Spec element that defines deployment profile and parameters associated
  with the application deployment. See the [Spec Attributes](#spec-attributes) section
  below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: spec
owner: ApplicationDeployment
domain_of:
- ApplicationDeployment
range: Spec
required: true

```
</details>