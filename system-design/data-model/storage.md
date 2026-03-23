

# Slot: storage 


_The amount of storage required for the application to run. This encompasses the installed application and the data it needs to store. The value is given in binary units (`Ki` = Kibibytes, `Mi` = Mebibytes, `Gi` = Gibibytes, `Ti` Tebibytes, `Pi` = Pebibytes, `Ei` = Exbibytes). This is defined by the application developer. After deployment of the application, the device MUST provide this amount of storage for the application_





URI: [https://specification.margo.org/data-model/storage](https://specification.margo.org/data-model/storage)
Alias: storage

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
| Regex Pattern | `^[0-9]+(Mi|Gi|Ki|Ti|Pi|Ei)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/storage |
| native | https://specification.margo.org/data-model/storage |




## LinkML Source

<details>
```yaml
name: storage
description: The amount of storage required for the application to run. This encompasses
  the installed application and the data it needs to store. The value is given in
  binary units (`Ki` = Kibibytes, `Mi` = Mebibytes, `Gi` = Gibibytes, `Ti` Tebibytes,
  `Pi` = Pebibytes, `Ei` = Exbibytes). This is defined by the application developer.
  After deployment of the application, the device MUST provide this amount of storage
  for the application
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: storage
domain_of:
- Resources
range: string
required: false
pattern: ^[0-9]+(Mi|Gi|Ki|Ti|Pi|Ei)$

```
</details>