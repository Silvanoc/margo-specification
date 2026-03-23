

# Slot: id 



URI: [https://specification.margo.org/data-model/id](https://specification.margo.org/data-model/id)
Alias: id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeploymentAnnotations](DeploymentAnnotations.md) | A class representing annotations |  no  |
| [ApplicationMetadata](ApplicationMetadata.md) | Metadata about the application |  no  |
| [Properties](Properties.md) |  |  no  |
| [HelmDeploymentProfileDescription](HelmDeploymentProfileDescription.md) |  |  no  |
| [DeploymentProfileDescription](DeploymentProfileDescription.md) | Represents a deployment configuration for the application |  no  |
| [ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE |
| Domain Of | [DeploymentAnnotations](DeploymentAnnotations.md), [ApplicationMetadata](ApplicationMetadata.md), [DeploymentProfileDescription](DeploymentProfileDescription.md), [Properties](Properties.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/id |
| native | https://specification.margo.org/data-model/id |




## LinkML Source

<details>
```yaml
name: id
alias: id
domain_of:
- DeploymentAnnotations
- ApplicationMetadata
- DeploymentProfileDescription
- Properties

```
</details>