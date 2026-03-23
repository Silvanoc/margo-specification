

# Slot: deploymentProfiles 


_Deployment profiles element specifying the types of deployments the application supports. See the [Deployment](#deploymentprofile-attributes) section below._





URI: [https://specification.margo.org/data-model/deploymentProfiles](https://specification.margo.org/data-model/deploymentProfiles)
Alias: deploymentProfiles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ApplicationDescription](ApplicationDescription.md) | Root class for an application description |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeploymentProfileDescription](DeploymentProfileDescription.md) |
| Domain Of | [ApplicationDescription](ApplicationDescription.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ApplicationDescription](ApplicationDescription.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/deploymentProfiles |
| native | https://specification.margo.org/data-model/deploymentProfiles |




## LinkML Source

<details>
```yaml
name: deploymentProfiles
description: Deployment profiles element specifying the types of deployments the application
  supports. See the [Deployment](#deploymentprofile-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: deploymentProfiles
owner: ApplicationDescription
domain_of:
- ApplicationDescription
range: DeploymentProfileDescription
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>