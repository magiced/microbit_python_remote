# microbit_python_remote
Description of how to control a BBC Microbit remotely using Python and Bluetooth

## Microbit address

BBC micro:bit [zugeg] -> ED:B9:4A:79:34:B4 -> _RawAdvData(adv=<_bleak_winrt_Windows_Devices_Bluetooth_Advertisement.BluetoothLEAdvertisementReceivedEventArgs object at 0x00000135EB0660B0>, scan=None)

microbit event service UUID
```
const uint16_t MicroBitEventService::serviceUUID               = 0x93af;
const uint16_t MicroBitEventService::charUUID[ mbbs_cIdxCOUNT] = { 0x9775, 0xb84c, 0x5404, 0x23c4 };
```

from MicroBitEventService.cpp
