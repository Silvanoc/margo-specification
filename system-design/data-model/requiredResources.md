

# Slot: requiredResources 


_Required resources element specifying the resources required to install the application. See the [Required Resources](#requiredresources-attributes) section below. The consequences (e.g., aborting / blocking the installation or execution of the application) of not meeting these required resources are not defined (yet) by margo._





URI: [https://specification.margo.org/data-model/requiredResources](https://specification.margo.org/data-model/requiredResources)
Alias: requiredResources

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) |  |  no  |
| [DeploymentProfileDescription](DeploymentProfileDescription.md) | Represents a deployment configuration for the application |  no  |
| [HelmDeploymentProfileDescription](HelmDeploymentProfileDescription.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resources](Resources.md) |
| Domain Of | [DeploymentProfileDescription](DeploymentProfileDescription.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DeploymentProfileDescription](DeploymentProfileDescription.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/requiredResources |
| native | https://specification.margo.org/data-model/requiredResources |




## LinkML Source

<details>
```yaml
name: requiredResources
description: Required resources element specifying the resources required to install
  the application. See the [Required Resources](#requiredresources-attributes) section
  below. The consequences (e.g., aborting / blocking the installation or execution
  of the application) of not meeting these required resources are not defined (yet)
  by margo.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: requiredResources
owner: DeploymentProfileDescription
domain_of:
- DeploymentProfileDescription
range: Resources
required: false

```
</details>