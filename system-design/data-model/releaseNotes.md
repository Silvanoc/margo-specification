

# Slot: releaseNotes 


_Statement about the changes for this application's release. The file should either be a markdown or PDF file._





URI: [https://specification.margo.org/data-model/releaseNotes](https://specification.margo.org/data-model/releaseNotes)
Alias: releaseNotes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CatalogApplicationMetadata](CatalogApplicationMetadata.md) | Metadata specific to the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [CatalogApplicationMetadata](CatalogApplicationMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CatalogApplicationMetadata](CatalogApplicationMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/releaseNotes |
| native | https://specification.margo.org/data-model/releaseNotes |




## LinkML Source

<details>
```yaml
name: releaseNotes
description: Statement about the changes for this application's release. The file
  should either be a markdown or PDF file.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: releaseNotes
owner: CatalogApplicationMetadata
domain_of:
- CatalogApplicationMetadata
range: string

```
</details>