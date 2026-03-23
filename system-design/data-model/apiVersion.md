

# Slot: apiVersion 



URI: [https://specification.margo.org/data-model/apiVersion](https://specification.margo.org/data-model/apiVersion)
Alias: apiVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ApplicationDeployment](ApplicationDeployment.md) | A class representing the desired state of an entity |  no  |
| [DeviceCapabilitiesManifest](DeviceCapabilitiesManifest.md) | Capabilities of a device on which applications can be deployed |  no  |
| [ApplicationDescription](ApplicationDescription.md) | Root class for an application description |  no  |
| [DeploymentStatusManifest](DeploymentStatusManifest.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE |
| Domain Of | [ApplicationDeployment](ApplicationDeployment.md), [ApplicationDescription](ApplicationDescription.md), [DeviceCapabilitiesManifest](DeviceCapabilitiesManifest.md), [DeploymentStatusManifest](DeploymentStatusManifest.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/apiVersion |
| native | https://specification.margo.org/data-model/apiVersion |




## LinkML Source

<details>
```yaml
name: apiVersion
alias: apiVersion
domain_of:
- ApplicationDeployment
- ApplicationDescription
- DeviceCapabilitiesManifest
- DeploymentStatusManifest

```
</details>