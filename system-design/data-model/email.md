

# Slot: email 


_Email address of the application's creator._





URI: [https://specification.margo.org/data-model/email](https://specification.margo.org/data-model/email)
Alias: email

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Author](Author.md) | Information about the application's author |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [string](string.md) |
| Domain Of | [Author](Author.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Author](Author.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `.*@[a-z0-9.-]*` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/email |
| native | https://specification.margo.org/data-model/email |




## LinkML Source

<details>
```yaml
name: email
description: Email address of the application's creator.
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: email
owner: Author
domain_of:
- Author
range: string
pattern: .*@[a-z0-9.-]*

```
</details>