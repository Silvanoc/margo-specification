

# Slot: architectures 


_The CPU architectures supported by the application. This can be e.g. amd64, x86_64, arm64, arm. See the [CpuArchitectureType](#cpuarchitecturetype) definition for all permissible values. Multiple arcitecture types can be specified, as the deployment profile may support multiple CPU architectures._





URI: [https://specification.margo.org/data-model/architectures](https://specification.margo.org/data-model/architectures)
Alias: architectures

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CPU](CPU.md) | CPU element specifying the CPU requirements for the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CpuArchitectureType](CpuArchitectureType.md) |
| Domain Of | [CPU](CPU.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CPU](CPU.md) |












## Identifier and Mapping Information
### Administrative Metadata

**Rank:** 20






### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/architectures |
| native | https://specification.margo.org/data-model/architectures |




## LinkML Source

<details>
```yaml
name: architectures
description: The CPU architectures supported by the application. This can be e.g.
  amd64, x86_64, arm64, arm. See the [CpuArchitectureType](#cpuarchitecturetype) definition
  for all permissible values. Multiple arcitecture types can be specified, as the
  deployment profile may support multiple CPU architectures.
from_schema: https://specification.margo.org/data-model
rank: 20
alias: architectures
owner: CPU
domain_of:
- CPU
range: CpuArchitectureType
required: false
multivalued: true
inlined: false

```
</details>