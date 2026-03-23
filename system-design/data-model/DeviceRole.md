# Enum: DeviceRole 



URI: [https://specification.margo.org/data-model/DeviceRole](https://specification.margo.org/data-model/DeviceRole)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| Standalone Cluster | None | Select this role to run Helm applications |
| Standalone Device | None | Select this role to run Compose applications |




## Slots

| Name | Description |
| ---  | --- |
| [roles](roles.md) | Element that defines the device role it can provide to the Margo environment |










## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model






## LinkML Source

<details>
```yaml
name: DeviceRole
from_schema: https://specification.margo.org/data-model
rank: 1000
permissible_values:
  Standalone Cluster:
    text: Standalone Cluster
    description: Select this role to run Helm applications. See [Edge compute devices](../../concepts/edge-compute-devices/devices#standalone-cluster-role-details)
      for more information.
  Standalone Device:
    text: Standalone Device
    description: Select this role to run Compose applications. See [Edge compute devices](../../concepts/edge-compute-devices/devices#standalone-device-role-details)
      for more information.

```
</details>