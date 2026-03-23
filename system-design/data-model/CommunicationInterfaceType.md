# Enum: CommunicationInterfaceType 



URI: [https://specification.margo.org/data-model/CommunicationInterfaceType](https://specification.margo.org/data-model/CommunicationInterfaceType)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ethernet | None | This type stands for an Ethernet interface |
| wifi | None | This type stands for an WiFi interface |
| cellular | None | This type stands for cellular communication technologies such as 5G, LTE, 3G,... |
| bluetooth | None | This type stands for a Bluetooth or Bluetooth Low-Energy (BLE) interface |
| usb | None | This type stands for a USB interface |
| canbus | None | This type stands for a CANBus interface |
| rs232 | None | This type stands for a RS232 interface |
| other | None | This type stands for any other communication interface not listed here |













## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model






## LinkML Source

<details>
```yaml
name: CommunicationInterfaceType
from_schema: https://specification.margo.org/data-model
rank: 1000
permissible_values:
  ethernet:
    text: ethernet
    description: This type stands for an Ethernet interface.
  wifi:
    text: wifi
    description: This type stands for an WiFi interface.
  cellular:
    text: cellular
    description: This type stands for cellular communication technologies such as
      5G, LTE, 3G, 2G, ....
  bluetooth:
    text: bluetooth
    description: This type stands for a Bluetooth or Bluetooth Low-Energy (BLE) interface.
  usb:
    text: usb
    description: This type stands for a USB interface.
  canbus:
    text: canbus
    description: This type stands for a CANBus interface.
  rs232:
    text: rs232
    description: This type stands for a RS232 interface.
  other:
    text: other
    description: This type stands for any other communication interface not listed
      here. The application developer MUST provide a description of the interface
      in the deployment profile's `description` field.

```
</details>