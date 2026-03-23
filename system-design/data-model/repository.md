

# Slot: repository 


_Repository location for the component._





URI: [https://specification.margo.org/data-model/repository](https://specification.margo.org/data-model/repository)
Alias: repository

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComponentProperties](ComponentProperties.md) | Properties dictionary for component deployment details |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [ComponentProperties](ComponentProperties.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ComponentProperties](ComponentProperties.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/repository |
| native | https://specification.margo.org/data-model/repository |




## LinkML Source

<details>
```yaml
name: repository
description: Repository location for the component.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: repository
owner: ComponentProperties
domain_of:
- ComponentProperties
range: string

```
</details>