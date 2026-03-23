

# Slot: application 


_Application element specifying the application specific metadata. See the [Application Metadata](#applicationmetadata-attributes) section below._





URI: [https://specification.margo.org/data-model/application](https://specification.margo.org/data-model/application)
Alias: application

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Catalog](Catalog.md) | Catalog metadata for displaying the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CatalogApplicationMetadata](CatalogApplicationMetadata.md) |
| Domain Of | [Catalog](Catalog.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Catalog](Catalog.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/application |
| native | https://specification.margo.org/data-model/application |




## LinkML Source

<details>
```yaml
name: application
description: Application element specifying the application specific metadata. See
  the [Application Metadata](#applicationmetadata-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: application
owner: Catalog
domain_of:
- Catalog
range: CatalogApplicationMetadata

```
</details>