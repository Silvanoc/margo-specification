

# Slot: interfaces 


_Interfaces element specifying the communication interfaces required to run the application. See the [Communication Interfaces](#communicationinterface-attributes) section below._





URI: [https://specification.margo.org/data-model/interfaces](https://specification.margo.org/data-model/interfaces)
Alias: interfaces

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Resources](Resources.md) | Required resources element specifying the resources required to install the a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CommunicationInterface](CommunicationInterface.md) |
| Domain Of | [Resources](Resources.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/interfaces |
| native | https://specification.margo.org/data-model/interfaces |




## LinkML Source

<details>
```yaml
name: interfaces
description: Interfaces element specifying the communication interfaces required to
  run the application. See the [Communication Interfaces](#communicationinterface-attributes)
  section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: interfaces
domain_of:
- Resources
range: CommunicationInterface
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>