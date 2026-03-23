

# Slot: kind 



URI: [https://specification.margo.org/data-model/kind](https://specification.margo.org/data-model/kind)
Alias: kind

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
| self | https://specification.margo.org/data-model/kind |
| native | https://specification.margo.org/data-model/kind |




## LinkML Source

<details>
```yaml
name: kind
alias: kind
domain_of:
- ApplicationDeployment
- ApplicationDescription
- DeviceCapabilitiesManifest
- DeploymentStatusManifest

```
</details>