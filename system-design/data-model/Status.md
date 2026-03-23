

# Slot: status 



URI: [https://specification.margo.org/data-model/status](https://specification.margo.org/data-model/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeploymentStatusManifest](DeploymentStatusManifest.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Status](Status.md) |
| Domain Of | [DeploymentStatusManifest](DeploymentStatusManifest.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DeploymentStatusManifest](DeploymentStatusManifest.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/status |
| native | https://specification.margo.org/data-model/status |




## LinkML Source

<details>
```yaml
name: status
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: status
owner: DeploymentStatusManifest
domain_of:
- DeploymentStatusManifest
range: Status
required: true

```
</details>