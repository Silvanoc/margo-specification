# Enum: CpuArchitectureType 



URI: [https://specification.margo.org/data-model/CpuArchitectureType](https://specification.margo.org/data-model/CpuArchitectureType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| amd64 | None | AMD 64-bit architecture |
| x86_64 | None | x86 64-bit architecture |
| arm64 | None | ARM 64-bit architecture |
| arm | None | ARM 32-bit architecture |
| riscv64 | None | RISC-V 64-bit architecture |
| other | None | Any other CPU architecture not listed here |




## Slots

| Name | Description |
| ---  | --- |
| [architectures](architectures.md) | The CPU architectures supported by the application |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model






## LinkML Source

<details>
```yaml
name: CpuArchitectureType
from_schema: https://specification.margo.org/data-model
rank: 1000
permissible_values:
  amd64:
    text: amd64
    description: AMD 64-bit architecture.
  x86_64:
    text: x86_64
    description: x86 64-bit architecture.
  arm64:
    text: arm64
    description: ARM 64-bit architecture.
  arm:
    text: arm
    description: ARM 32-bit architecture.
  riscv64:
    text: riscv64
    description: RISC-V 64-bit architecture.
  other:
    text: other
    description: Any other CPU architecture not listed here. The application developer
      MUST provide a description of the architecture in the deployment profile's `description`
      field.

```
</details>