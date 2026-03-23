

# Slot: value 


_The parameter's default value.  Accepted data types are string, integer, double, boolean, array[string], array[integer], array[double], array[boolean]._





URI: [https://specification.margo.org/data-model/value](https://specification.margo.org/data-model/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Parameter](Parameter.md) | Defines a configurable parameter for the application |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE&nbsp;or&nbsp;<br />[boolean](boolean.md)&nbsp;or&nbsp;<br />[integer](integer.md)&nbsp;or&nbsp;<br />[string](string.md)&nbsp;or&nbsp;<br />[double](double.md) |
| Domain Of | [Parameter](Parameter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Parameter](Parameter.md) |


<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'boolean'})
- AnonymousSlotExpression({'range': 'integer'})
- AnonymousSlotExpression({'range': 'double'})
- AnonymousSlotExpression({'range': 'string'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/value |
| native | https://specification.margo.org/data-model/value |




## LinkML Source

<details>
```yaml
name: value
description: The parameter's default value.  Accepted data types are string, integer,
  double, boolean, array[string], array[integer], array[double], array[boolean].
from_schema: https://specification.margo.org/data-model
rank: 1000
alias: value
owner: Parameter
domain_of:
- Parameter
any_of:
- range: boolean
- range: integer
- range: double
- range: string

```
</details>