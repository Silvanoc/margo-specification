

# Slot: pointer 


_The name of the parameter in the deployment configuration.  For Helm deployments, this is the dot notation for the matching element in the `values.yaml` file. This follows the same naming convention you would use with the `--set` command line argument with the `helm install` command.  For compose deployments, this is the name of the environment variable to set._





URI: [https://specification.margo.org/data-model/pointer](https://specification.margo.org/data-model/pointer)
Alias: pointer

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Target](Target.md) | Specifies where the parameter applies in the deployment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Target](Target.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Target](Target.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/pointer |
| native | https://specification.margo.org/data-model/pointer |




## LinkML Source

<details>
```yaml
name: pointer
description: The name of the parameter in the deployment configuration.  For Helm
  deployments, this is the dot notation for the matching element in the `values.yaml`
  file. This follows the same naming convention you would use with the `--set` command
  line argument with the `helm install` command.  For compose deployments, this is
  the name of the environment variable to set.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: pointer
owner: Target
domain_of:
- Target
range: string
required: true

```
</details>