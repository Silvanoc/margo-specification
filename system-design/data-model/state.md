# Enum: State 



URI: [https://specification.margo.org/data-model/State](https://specification.margo.org/data-model/State)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| pending | None |  |
| installing | None |  |
| installed | None |  |
| failed | None |  |
| removing | None |  |
| removed | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [state](state.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model






## LinkML Source

<details>
```yaml
name: State
from_schema: https://specification.margo.org/data-model
rank: 1000
permissible_values:
  pending:
    text: pending
  installing:
    text: installing
  installed:
    text: installed
  failed:
    text: failed
  removing:
    text: removing
  removed:
    text: removed

```
</details>