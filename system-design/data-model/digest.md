

# Slot: digest 



URI: [https://specification.margo.org/data-model/digest](https://specification.margo.org/data-model/digest)
Alias: digest

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Deployment](Deployment.md) | List of deployment objects describing each workload |  no  |
| [Bundle](Bundle.md) | Describes an archive containing all referenced ApplicationDeployment YAMLs |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE |
| Domain Of | [Bundle](Bundle.md), [Deployment](Deployment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/digest |
| native | https://specification.margo.org/data-model/digest |




## LinkML Source

<details>
```yaml
name: digest
alias: digest
domain_of:
- Bundle
- Deployment

```
</details>