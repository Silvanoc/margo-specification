

# Slot: memory 


_The minimum amount of memory required. The value is given in binary units (`Ki` = Kibibytes, `Mi` = Mebibytes, `Gi` = Gibibytes). This is defined by the application developer. After deployment of the application, the device MUST provide this amount of memory for the application._





URI: [https://specification.margo.org/data-model/memory](https://specification.margo.org/data-model/memory)
Alias: memory

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resources](Resources.md) | Required resources element specifying the resources required to install the a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Resources](Resources.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[0-9]+(Mi|Gi|Ki)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/memory |
| native | https://specification.margo.org/data-model/memory |




## LinkML Source

<details>
```yaml
name: memory
description: The minimum amount of memory required. The value is given in binary units
  (`Ki` = Kibibytes, `Mi` = Mebibytes, `Gi` = Gibibytes). This is defined by the application
  developer. After deployment of the application, the device MUST provide this amount
  of memory for the application.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: memory
domain_of:
- Resources
range: string
required: false
pattern: ^[0-9]+(Mi|Gi|Ki)$

```
</details>