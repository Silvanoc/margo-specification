

# Slot: deployments 


_List of deployment objects describing each workload._





URI: [https://specification.margo.org/data-model/deployments](https://specification.margo.org/data-model/deployments)
Alias: deployments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DesiredStateManifest](DesiredStateManifest.md) | Manifest from the Workload Fleet Manager, representing the complete desired w... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Deployment](Deployment.md) |
| Domain Of | [DesiredStateManifest](DesiredStateManifest.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DesiredStateManifest](DesiredStateManifest.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/deployments |
| native | https://specification.margo.org/data-model/deployments |




## LinkML Source

<details>
```yaml
name: deployments
description: List of deployment objects describing each workload.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: deployments
owner: DesiredStateManifest
domain_of:
- DesiredStateManifest
range: Deployment
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>