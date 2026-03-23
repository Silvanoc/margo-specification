

# Slot: author 


_Author element specifying metadata about the application's author. See the [Author Metadata](#author-attributes) section below._





URI: [https://specification.margo.org/data-model/author](https://specification.margo.org/data-model/author)
Alias: author

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Catalog](Catalog.md) | Catalog metadata for displaying the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Author](Author.md) |
| Domain Of | [Catalog](Catalog.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | https://specification.margo.org/data-model/author |
| native | https://specification.margo.org/data-model/author |




## LinkML Source

<details>
```yaml
name: author
description: Author element specifying metadata about the application's author. See
  the [Author Metadata](#author-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: author
owner: Catalog
domain_of:
- Catalog
range: Author
multivalued: true
inlined: true
inlined_as_list: true

```
</details>