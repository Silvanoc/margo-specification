

# Slot: sections 


_Sections are used to group related parameters together, so it is possible to present a user interface with a logical grouping of the parameters in each section. See the [Section](#section-attributes) section below._





URI: [https://specification.margo.org/data-model/sections](https://specification.margo.org/data-model/sections)
Alias: sections

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Configuration](Configuration.md) | Configuration layout and validation rules |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Section](Section.md) |
| Domain Of | [Configuration](Configuration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Configuration](Configuration.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/sections |
| native | https://specification.margo.org/data-model/sections |




## LinkML Source

<details>
```yaml
name: sections
description: Sections are used to group related parameters together, so it is possible
  to present a user interface with a logical grouping of the parameters in each section.
  See the [Section](#section-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: sections
owner: Configuration
domain_of:
- Configuration
range: Section
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>