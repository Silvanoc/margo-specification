

# Slot: tags 


_An array of strings that can be used to provide additional context for the application in a user interface to assist with task such as categorizing, searching, etc._





URI: [https://specification.margo.org/data-model/tags](https://specification.margo.org/data-model/tags)
Alias: tags

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
| Multivalued | Yes |
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
| self | https://specification.margo.org/data-model/tags |
| native | https://specification.margo.org/data-model/tags |




## LinkML Source

<details>
```yaml
name: tags
description: An array of strings that can be used to provide additional context for
  the application in a user interface to assist with task such as categorizing, searching,
  etc.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: tags
owner: CatalogApplicationMetadata
domain_of:
- CatalogApplicationMetadata
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>