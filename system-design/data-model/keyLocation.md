

# Slot: keyLocation 


_URL for the public key used to validate a digitally signed package._





URI: [https://specification.margo.org/data-model/keyLocation](https://specification.margo.org/data-model/keyLocation)
Alias: keyLocation

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
| self | https://specification.margo.org/data-model/keyLocation |
| native | https://specification.margo.org/data-model/keyLocation |




## LinkML Source

<details>
```yaml
name: keyLocation
description: URL for the public key used to validate a digitally signed package.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: keyLocation
owner: ComponentProperties
domain_of:
- ComponentProperties
range: string

```
</details>