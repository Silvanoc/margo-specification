

# Slot: namespace 


_When deploying to Kubernetes, the namespace the manifest is added under. The namespace is chosen by the workload orchestration solution vendor._





URI: [https://specification.margo.org/data-model/namespace](https://specification.margo.org/data-model/namespace)
Alias: namespace

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeploymentMetadata](DeploymentMetadata.md) | Metadata associated with the desired state |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [DeploymentMetadata](DeploymentMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DeploymentMetadata](DeploymentMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/namespace |
| native | https://specification.margo.org/data-model/namespace |




## LinkML Source

<details>
```yaml
name: namespace
description: When deploying to Kubernetes, the namespace the manifest is added under.
  The namespace is chosen by the workload orchestration solution vendor.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: namespace
owner: DeploymentMetadata
domain_of:
- DeploymentMetadata
range: string
required: true

```
</details>