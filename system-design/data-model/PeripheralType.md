# Enum: PeripheralType 



URI: [https://specification.margo.org/data-model/PeripheralType](https://specification.margo.org/data-model/PeripheralType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| gpu | None | This type stands for a Graphics Processing Unit (GPU) peripheral |
| display | None | This type stands for a display peripheral |
| camera | None | This type stands for a camera peripheral |
| microphone | None | This type stands for a microphone peripheral |
| speaker | None | This type stands for a speaker peripheral |
| other | None | This type stands for any other peripheral not listed here |













## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model






## LinkML Source

<details>
```yaml
name: PeripheralType
from_schema: https://specification.margo.org/data-model
rank: 1000
permissible_values:
  gpu:
    text: gpu
    description: This type stands for a Graphics Processing Unit (GPU) peripheral.
  display:
    text: display
    description: This type stands for a display peripheral.
  camera:
    text: camera
    description: This type stands for a camera peripheral.
  microphone:
    text: microphone
    description: This type stands for a microphone peripheral.
  speaker:
    text: speaker
    description: This type stands for a speaker peripheral.
  other:
    text: other
    description: This type stands for any other peripheral not listed here. The application
      developer MUST provide a description of the peripheral in the deployment profile's
      `description` field.

```
</details>