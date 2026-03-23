

# Slot: timeout 


_Time to wait for component installation to complete, formatted as "##m##s"._





URI: [https://specification.margo.org/data-model/timeout](https://specification.margo.org/data-model/timeout)
Alias: timeout

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
| self | https://specification.margo.org/data-model/timeout |
| native | https://specification.margo.org/data-model/timeout |




## LinkML Source

<details>
```yaml
name: timeout
description: Time to wait for component installation to complete, formatted as "##m##s".
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: timeout
owner: ComponentProperties
domain_of:
- ComponentProperties
range: string

```
</details>