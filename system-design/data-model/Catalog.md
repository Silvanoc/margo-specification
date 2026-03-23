

# Slot: catalog 


_Catalog element specifying the application's metadata for enabling its discovery. See the [Catalog](#catalog-attributes) section below._





URI: [https://specification.margo.org/data-model/catalog](https://specification.margo.org/data-model/catalog)
Alias: catalog

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ApplicationMetadata](ApplicationMetadata.md) | Metadata about the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Catalog](Catalog.md) |
| Domain Of | [ApplicationMetadata](ApplicationMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ApplicationMetadata](ApplicationMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/catalog |
| native | https://specification.margo.org/data-model/catalog |




## LinkML Source

<details>
```yaml
name: catalog
description: Catalog element specifying the application's metadata for enabling its
  discovery. See the [Catalog](#catalog-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: catalog
owner: ApplicationMetadata
domain_of:
- ApplicationMetadata
range: Catalog
required: true

```
</details>