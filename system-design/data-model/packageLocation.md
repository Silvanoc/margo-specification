

# Slot: packageLocation 


_URL indicating the Compose package's location._





URI: [https://specification.margo.org/data-model/packageLocation](https://specification.margo.org/data-model/packageLocation)
Alias: packageLocation

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
| self | https://specification.margo.org/data-model/packageLocation |
| native | https://specification.margo.org/data-model/packageLocation |




## LinkML Source

<details>
```yaml
name: packageLocation
description: URL indicating the Compose package's location.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: packageLocation
owner: ComponentProperties
domain_of:
- ComponentProperties
range: string

```
</details>