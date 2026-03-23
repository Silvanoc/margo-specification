

# Slot: type 


_Defines the type of this deployment configuration for the application.  The allowed values are `helm.v3`, to indicate the deployment profile's format is Helm version 3,  and `compose` to indicate the deployment profile's format is a Compose file.  When installing the application on a device supporting the Kubernetes platform, all `helm.v3` components,  and only `helm.v3` components, will be provided to the device in same order they are listed in the application description file.  When installing the application on a device supporting Compose, all `compose` components,  and only `compose` components, will be provided to the device in the same order they are listed in the application description file.  The device will install the components in the same order they are listed in the application description file._





URI: [https://specification.margo.org/data-model/type](https://specification.margo.org/data-model/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HelmDeploymentProfileDescription](HelmDeploymentProfileDescription.md) |  |  yes  |
| [ComposeDeploymentProfile](ComposeDeploymentProfile.md) |  |  yes  |
| [DeploymentProfileDescription](DeploymentProfileDescription.md) | Represents a deployment configuration for the application |  no  |
| [Peripheral](Peripheral.md) | Peripheral hardware of a device |  no  |
| [ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) |  |  yes  |
| [HelmDeploymentProfile](HelmDeploymentProfile.md) |  |  yes  |
| [CommunicationInterface](CommunicationInterface.md) | Communication interface of a device |  no  |
| [DeploymentProfile](DeploymentProfile.md) | Represents a deployment configuration for the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [DeploymentProfile](DeploymentProfile.md), [Peripheral](Peripheral.md), [CommunicationInterface](CommunicationInterface.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(helm\.v3|compose)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/type |
| native | https://specification.margo.org/data-model/type |




## LinkML Source

<details>
```yaml
name: type
description: Defines the type of this deployment configuration for the application.  The
  allowed values are `helm.v3`, to indicate the deployment profile's format is Helm
  version 3,  and `compose` to indicate the deployment profile's format is a Compose
  file.  When installing the application on a device supporting the Kubernetes platform,
  all `helm.v3` components,  and only `helm.v3` components, will be provided to the
  device in same order they are listed in the application description file.  When
  installing the application on a device supporting Compose, all `compose` components,  and
  only `compose` components, will be provided to the device in the same order they
  are listed in the application description file.  The device will install the components
  in the same order they are listed in the application description file.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: type
domain_of:
- DeploymentProfile
- Peripheral
- CommunicationInterface
range: string
required: true
pattern: ^(helm\.v3|compose)$

```
</details>