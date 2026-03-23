

# Slot: error 



URI: [https://specification.margo.org/data-model/error](https://specification.margo.org/data-model/error)
Alias: error

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Status](Status.md) |  |  no  |
| [ComponentStatus](ComponentStatus.md) | Status of a component deployment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Error](Error.md) |
| Domain Of | [Status](Status.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/error |
| native | https://specification.margo.org/data-model/error |




## LinkML Source

<details>
```yaml
name: error
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: error
domain_of:
- Status
range: Error

```
</details>