

# Slot: components 


_Component element indicating the components to deploy when installing the application.  See the [Component](#component-attributes) section below._





URI: [https://specification.margo.org/data-model/components](https://specification.margo.org/data-model/components)
Alias: components

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Target](Target.md) | Specifies where the parameter applies in the deployment |  no  |
| [HelmDeploymentProfileDescription](HelmDeploymentProfileDescription.md) |  |  yes  |
| [ComposeDeploymentProfile](ComposeDeploymentProfile.md) |  |  yes  |
| [DeploymentProfileDescription](DeploymentProfileDescription.md) | Represents a deployment configuration for the application |  no  |
| [ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) |  |  yes  |
| [HelmDeploymentProfile](HelmDeploymentProfile.md) |  |  yes  |
| [DeploymentProfile](DeploymentProfile.md) | Represents a deployment configuration for the application |  no  |
| [DeploymentStatusManifest](DeploymentStatusManifest.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Component](Component.md) |
| Domain Of | [DeploymentProfile](DeploymentProfile.md), [Target](Target.md), [DeploymentStatusManifest](DeploymentStatusManifest.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/components |
| native | https://specification.margo.org/data-model/components |




## LinkML Source

<details>
```yaml
name: components
description: Component element indicating the components to deploy when installing
  the application.  See the [Component](#component-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: components
domain_of:
- DeploymentProfile
- Target
- DeploymentStatusManifest
range: Component
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>