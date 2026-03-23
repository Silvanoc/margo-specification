

# Slot: mediaType 


_MUST be application/vnd.margo.bundle.v1+tar+gzip, which denotes a gzip-compressed tar archive (commonly delivered as a .tar.gz) whose root contains one or more ApplicationDeployment YAML files. Servers MUST set the HTTP Content-Type to this media type. The archive MUST contain exactly the set of YAML files referenced by deployments._





URI: [https://specification.margo.org/data-model/mediaType](https://specification.margo.org/data-model/mediaType)
Alias: mediaType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Bundle](Bundle.md) | Describes an archive containing all referenced ApplicationDeployment YAMLs |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Bundle](Bundle.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Bundle](Bundle.md) |


<details>
<summary>Additional Constraints</summary>
**Must Equal:** `application/vnd.margo.bundle.v1+tar+gzip`

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/mediaType |
| native | https://specification.margo.org/data-model/mediaType |




## LinkML Source

<details>
```yaml
name: mediaType
description: MUST be application/vnd.margo.bundle.v1+tar+gzip, which denotes a gzip-compressed
  tar archive (commonly delivered as a .tar.gz) whose root contains one or more ApplicationDeployment
  YAML files. Servers MUST set the HTTP Content-Type to this media type. The archive
  MUST contain exactly the set of YAML files referenced by deployments.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: mediaType
owner: Bundle
domain_of:
- Bundle
range: string
required: true
equals_string: application/vnd.margo.bundle.v1+tar+gzip

```
</details>