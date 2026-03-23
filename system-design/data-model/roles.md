

# Slot: roles 


_Element that defines the device role it can provide to the Margo environment. MUST be one of the following: Standalone Cluster, or Standalone Device_





URI: [https://specification.margo.org/data-model/roles](https://specification.margo.org/data-model/roles)
Alias: roles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Properties](Properties.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DeviceRole](DeviceRole.md) |
| Domain Of | [Properties](Properties.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Properties](Properties.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/roles |
| native | https://specification.margo.org/data-model/roles |




## LinkML Source

<details>
```yaml
name: roles
description: 'Element that defines the device role it can provide to the Margo environment.
  MUST be one of the following: Standalone Cluster, or Standalone Device'
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: roles
owner: Properties
domain_of:
- Properties
range: DeviceRole
required: true
multivalued: true
inlined: false

```
</details>