

# Slot: annotations 


_Defines the application ID and unique identifier associated to the deployment specification. Needs to be assigned by the Workload Orchestration Software. See the [Annotation Attributes](#annotations-attributes) section below._





URI: [https://specification.margo.org/data-model/annotations](https://specification.margo.org/data-model/annotations)
Alias: annotations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeploymentMetadata](DeploymentMetadata.md) | Metadata associated with the desired state |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeploymentAnnotations](DeploymentAnnotations.md) |
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
| self | https://specification.margo.org/data-model/annotations |
| native | https://specification.margo.org/data-model/annotations |




## LinkML Source

<details>
```yaml
name: annotations
description: Defines the application ID and unique identifier associated to the deployment
  specification. Needs to be assigned by the Workload Orchestration Software. See
  the [Annotation Attributes](#annotations-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: annotations
owner: DeploymentMetadata
domain_of:
- DeploymentMetadata
range: DeploymentAnnotations
required: true

```
</details>