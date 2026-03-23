

# Slot: cores 


_The required amount of CPU cores the application must use to run in its full functionality. Specified as decimal units of CPU cores (e.g., `0.5` is half a core). This is defined by the application developer. After deployment of the application, the device MUST provide this number of CPU cores for the application._





URI: [https://specification.margo.org/data-model/cores](https://specification.margo.org/data-model/cores)
Alias: cores

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CPU](CPU.md) | CPU element specifying the CPU requirements for the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [double](double.md) |
| Domain Of | [CPU](CPU.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CPU](CPU.md) |












## Identifier and Mapping Information
### Administrative Metadata

**Rank:** 10






### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/cores |
| native | https://specification.margo.org/data-model/cores |




## LinkML Source

<details>
```yaml
name: cores
description: The required amount of CPU cores the application must use to run in its
  full functionality. Specified as decimal units of CPU cores (e.g., `0.5` is half
  a core). This is defined by the application developer. After deployment of the application,
  the device MUST provide this number of CPU cores for the application.
from_schema: https://specification.margo.org/data-model
rank: 10
alias: cores
owner: CPU
domain_of:
- CPU
range: double
required: true

```
</details>