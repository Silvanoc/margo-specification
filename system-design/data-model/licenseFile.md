

# Slot: licenseFile 


_Link to the file that details the application's license. The file should either be a plain text, markdown or PDF file._





URI: [https://specification.margo.org/data-model/licenseFile](https://specification.margo.org/data-model/licenseFile)
Alias: licenseFile

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
| self | https://specification.margo.org/data-model/licenseFile |
| native | https://specification.margo.org/data-model/licenseFile |




## LinkML Source

<details>
```yaml
name: licenseFile
description: Link to the file that details the application's license. The file should
  either be a plain text, markdown or PDF file.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: licenseFile
owner: CatalogApplicationMetadata
domain_of:
- CatalogApplicationMetadata
range: string

```
</details>