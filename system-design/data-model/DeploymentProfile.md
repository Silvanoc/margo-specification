

# Slot: deploymentProfile 


_Section that defines deployment details including type and components._





URI: [https://specification.margo.org/data-model/deploymentProfile](https://specification.margo.org/data-model/deploymentProfile)
Alias: deploymentProfile

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Spec](Spec.md) | Specification details of the desired state |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeploymentProfile](DeploymentProfile.md) |
| Domain Of | [Spec](Spec.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Spec](Spec.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/deploymentProfile |
| native | https://specification.margo.org/data-model/deploymentProfile |




## LinkML Source

<details>
```yaml
name: deploymentProfile
description: Section that defines deployment details including type and components.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: deploymentProfile
owner: Spec
domain_of:
- Spec
range: DeploymentProfile
required: true

```
</details>