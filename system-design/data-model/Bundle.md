

# Slot: bundle 


_Package optimization containing multiple ApplicationDeployment YAMLs._





URI: [https://specification.margo.org/data-model/bundle](https://specification.margo.org/data-model/bundle)
Alias: bundle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DesiredStateManifest](DesiredStateManifest.md) | Manifest from the Workload Fleet Manager, representing the complete desired w... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Bundle](Bundle.md) |
| Domain Of | [DesiredStateManifest](DesiredStateManifest.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | https://specification.margo.org/data-model/bundle |
| native | https://specification.margo.org/data-model/bundle |




## LinkML Source

<details>
```yaml
name: bundle
description: Package optimization containing multiple ApplicationDeployment YAMLs.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: bundle
owner: DesiredStateManifest
domain_of:
- DesiredStateManifest
range: Bundle
required: true

```
</details>