

# Slot: manifestVersion 



URI: [https://specification.margo.org/data-model/manifestVersion](https://specification.margo.org/data-model/manifestVersion)
Alias: manifestVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DesiredStateManifest](DesiredStateManifest.md) | Manifest from the Workload Fleet Manager, representing the complete desired w... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [integer](integer.md) |
| Domain Of | [DesiredStateManifest](DesiredStateManifest.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DesiredStateManifest](DesiredStateManifest.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | 1 |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/manifestVersion |
| native | https://specification.margo.org/data-model/manifestVersion |




## LinkML Source

<details>
```yaml
name: manifestVersion
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: manifestVersion
owner: DesiredStateManifest
domain_of:
- DesiredStateManifest
range: integer
required: true
minimum_value: 1

```
</details>