

# Slot: description 



URI: [https://specification.margo.org/data-model/description](https://specification.margo.org/data-model/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Setting](Setting.md) | Individual configuration settings |  no  |
| [ApplicationMetadata](ApplicationMetadata.md) | Metadata about the application |  no  |
| [HelmDeploymentProfileDescription](HelmDeploymentProfileDescription.md) |  |  no  |
| [DeploymentProfileDescription](DeploymentProfileDescription.md) | Represents a deployment configuration for the application |  no  |
| [ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE |
| Domain Of | [ApplicationMetadata](ApplicationMetadata.md), [DeploymentProfileDescription](DeploymentProfileDescription.md), [Setting](Setting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/description |
| native | https://specification.margo.org/data-model/description |




## LinkML Source

<details>
```yaml
name: description
alias: description
domain_of:
- ApplicationMetadata
- DeploymentProfileDescription
- Setting

```
</details>