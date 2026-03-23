

# Slot: settings 


_Settings are used to provide instructions to the workload orchestration software vendor for displaying parameters to the user. A user MUST be able to provide values for all settings. See the [Setting](#setting-attributes) section below._





URI: [https://specification.margo.org/data-model/settings](https://specification.margo.org/data-model/settings)
Alias: settings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Section](Section.md) | Named sections within the configuration layout |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Setting](Setting.md) |
| Domain Of | [Section](Section.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Section](Section.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/settings |
| native | https://specification.margo.org/data-model/settings |




## LinkML Source

<details>
```yaml
name: settings
description: Settings are used to provide instructions to the workload orchestration
  software vendor for displaying parameters to the user. A user MUST be able to provide
  values for all settings. See the [Setting](#setting-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: settings
owner: Section
domain_of:
- Section
range: Setting
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>