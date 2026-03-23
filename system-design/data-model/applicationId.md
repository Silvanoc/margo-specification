

# Slot: applicationId 


_An identifier for the application. The id is used to help create unique identifiers where required, such as namespaces. The id must be lower case letters and numbers and MAY contain dashes. Uppercase letters, underscores and periods MUST NOT be used. The id MUST NOT be more than 200 characters. The applicationId MUST match the associated application package Metadata "id" attribute._





URI: [https://specification.margo.org/data-model/applicationId](https://specification.margo.org/data-model/applicationId)
Alias: applicationId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DeploymentAnnotations](DeploymentAnnotations.md) | A class representing annotations |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [DeploymentAnnotations](DeploymentAnnotations.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DeploymentAnnotations](DeploymentAnnotations.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[-a-z0-9]{1,200}$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/applicationId |
| native | https://specification.margo.org/data-model/applicationId |




## LinkML Source

<details>
```yaml
name: applicationId
description: An identifier for the application. The id is used to help create unique
  identifiers where required, such as namespaces. The id must be lower case letters
  and numbers and MAY contain dashes. Uppercase letters, underscores and periods MUST
  NOT be used. The id MUST NOT be more than 200 characters. The applicationId MUST
  match the associated application package Metadata "id" attribute.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: applicationId
owner: DeploymentAnnotations
domain_of:
- DeploymentAnnotations
range: string
required: true
pattern: ^[-a-z0-9]{1,200}$

```
</details>