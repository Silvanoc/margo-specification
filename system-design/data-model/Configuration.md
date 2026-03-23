

# Slot: configuration 


_Configuration element specifying how parameters should be displayed to the user for setting the value as well as the rules to use to validate the user's input. See the [Configuration](#configuration-attributes) section below._





URI: [https://specification.margo.org/data-model/configuration](https://specification.margo.org/data-model/configuration)
Alias: configuration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ApplicationDescription](ApplicationDescription.md) | Root class for an application description |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Configuration](Configuration.md) |
| Domain Of | [ApplicationDescription](ApplicationDescription.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ApplicationDescription](ApplicationDescription.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/configuration |
| native | https://specification.margo.org/data-model/configuration |




## LinkML Source

<details>
```yaml
name: configuration
description: Configuration element specifying how parameters should be displayed to
  the user for setting the value as well as the rules to use to validate the user's
  input. See the [Configuration](#configuration-attributes) section below.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: configuration
owner: ApplicationDescription
domain_of:
- ApplicationDescription
range: Configuration

```
</details>