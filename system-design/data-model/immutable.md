

# Slot: immutable 


_If true, indicates the parameter value MUST not be changed once it has been set and used to install the application. Default is false if not provided._





URI: [https://specification.margo.org/data-model/immutable](https://specification.margo.org/data-model/immutable)
Alias: immutable

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Setting](Setting.md) | Individual configuration settings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [boolean](boolean.md) |
| Domain Of | [Setting](Setting.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Setting](Setting.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/immutable |
| native | https://specification.margo.org/data-model/immutable |




## LinkML Source

<details>
```yaml
name: immutable
description: If true, indicates the parameter value MUST not be changed once it has
  been set and used to install the application. Default is false if not provided.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: immutable
owner: Setting
domain_of:
- Setting
range: boolean

```
</details>