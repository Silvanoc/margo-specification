

# Slot: version 


_The application's version._





URI: [https://specification.margo.org/data-model/version](https://specification.margo.org/data-model/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ApplicationMetadata](ApplicationMetadata.md) | Metadata about the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [ApplicationMetadata](ApplicationMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ApplicationMetadata](ApplicationMetadata.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/version |
| native | https://specification.margo.org/data-model/version |




## LinkML Source

<details>
```yaml
name: version
description: The application's version.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: version
owner: ApplicationMetadata
domain_of:
- ApplicationMetadata
range: string
required: true

```
</details>