

# Slot: wait 


_If True, indicates the device waits for the component installation to complete._





URI: [https://specification.margo.org/data-model/wait](https://specification.margo.org/data-model/wait)
Alias: wait

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComponentProperties](ComponentProperties.md) | Properties dictionary for component deployment details |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [boolean](boolean.md) |
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
| self | https://specification.margo.org/data-model/wait |
| native | https://specification.margo.org/data-model/wait |




## LinkML Source

<details>
```yaml
name: wait
description: If True, indicates the device waits for the component installation to
  complete.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: wait
owner: ComponentProperties
domain_of:
- ComponentProperties
range: boolean

```
</details>