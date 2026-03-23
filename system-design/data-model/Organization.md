

# Slot: organization 


_Organization element specifying metadata about the organization/company providing the application. See the [Organization Metadata](#organization-attributes) section below._





URI: [https://specification.margo.org/data-model/organization](https://specification.margo.org/data-model/organization)
Alias: organization

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Catalog](Catalog.md) | Catalog metadata for displaying the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organization](Organization.md) |
| Domain Of | [Catalog](Catalog.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | https://specification.margo.org/data-model/organization |
| native | https://specification.margo.org/data-model/organization |




## LinkML Source

<details>
```yaml
name: organization
description: Organization element specifying metadata about the organization/company
  providing the application. See the [Organization Metadata](#organization-attributes)
  section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: organization
owner: Catalog
domain_of:
- Catalog
range: Organization
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>