

# Slot: resources 


_Element that defines the device's resources available to the application deployed on the device. See the [Resources Attributes](#resources-attributes) section below._





URI: [https://specification.margo.org/data-model/resources](https://specification.margo.org/data-model/resources)
Alias: resources

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Properties](Properties.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Resources](Resources.md) |
| Domain Of | [Properties](Properties.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | https://specification.margo.org/data-model/resources |
| native | https://specification.margo.org/data-model/resources |




## LinkML Source

<details>
```yaml
name: resources
description: Element that defines the device's resources available to the application
  deployed on the device. See the [Resources Attributes](#resources-attributes) section
  below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: resources
owner: Properties
domain_of:
- Properties
range: Resources
required: true

```
</details>