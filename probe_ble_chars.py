#import bleak (https://pypi.org/project/bleak/)
"""
----------------
XPC Reader
----------------
Operation:
    1) Connects and displays services with read characteristics
    2) If Nordic DFU service is found, returns PASS

"""
import os
import sys
import signal
import platform
import asyncio
import logging
import timeit
import atexit
import codecs
import time
import traceback

from bleak import BleakClient
from bleak.uuids import uuid16_dict
from bleak import BleakScanner

NOT_FOUND_LABEL = "NOT FOUND"
UNDEFINED_LABEL = "UNDEFINED"

address = NOT_FOUND_LABEL
uuid = UNDEFINED_LABEL
model = UNDEFINED_LABEL
bdate = UNDEFINED_LABEL 

DFU_SERVICE_LABEL = "Secure DFU Service"
DFU_RESULT_LABEL  = "Secure DFU Service identified: "
DEVICE_NAME_UUID = "00002a00-0000-1000-8000-00805f9b34fb"
DEVICE_NAME_LABEL = "Device Name: "
APPEARANCE_UUID = "00002a01-0000-1000-8000-00805f9b34fb"
CONNECTION_PARAMETERS_UUID = "00002a04-0000-1000-8000-00805f9b34fb"
CENTRAL_ADDRESS_RESOLUTION_UUID = "00002aa6-0000-1000-8000-00805f9b34fb"
MANUFACTURER_NAME_UUID = "00002a29-0000-1000-8000-00805f9b34fb"
MANUFACTURER_NAME_LABEL = "Manufacturer: "
MODEL_NUMBER_STRING_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
MODEL_NUMBER_STRING_LABEL = "Model Number String: "
SERIAL_NUMBER_UUID = "00002a25-0000-1000-8000-00805f9b34fb"
SERIAL_NUMBER_LABEL = "Board Serial Number: "
HARDWARE_REVISION_UUID = "00002a27-0000-1000-8000-00805f9b34fb"
HARDWARE_REVISION_LABEL = "Hardware Revision: "
FIRMWARE_REVISION_UUID = "00002a26-0000-1000-8000-00805f9b34fb"
FIRMWARE_REVISION_LABEL = "Firmware Revision: "
BATTERY_LEVEL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
BATTERY_LEVEL_LABEL = "Battery Level: "
BATTERY_TEMPERATURE_UUID = "bd9d2df9-c6fe-4516-87cf-96e307626be4"
BATTERY_WARNING_UUID = "bd9d2dfb-c6fe-4516-87cf-96e307626be4"
UIN_UUID = "c730d64a-5e58-5643-5444-f74d8b9ba87f"
UIN_LABEL = "UIN: "
BUILD_DATE_UUID = "c730d64b-5e58-5643-5444-f74d8b9ba87f"
BUILD_DATE_LABEL = "Build date: "
MOTOR_ENABLE_UUID = "f69f1e70-5259-4dff-b77c-10e04eb2be96"
MOTOR_AMPS_UUID = "f69f1e6e-5259-4dff-b77c-10e04eb2be96"
MOTOR_TEMP_UUID = "f69f1e6d-5259-4dff-b77c-10e04eb2be96"
MOTOR_RPM_UUID = "f69f1e6c-5259-4dff-b77c-10e04eb2be96"
NORDIC_DFU_SERVICE_UUID = "0000fe59-0000-1000-8000-00805f9b34fb"   

async def run(address, debug=False):

    global result

    print('Connecting to XPC')
    for i in range (5):
        print(f"Attempt: {i}")
        try: 
            async with BleakClient(address) as client:
                print('Connnected')

                client.services.get_descriptor

                for service in client.services:
                    for char in service.characteristics:
                        print(char)
                        if "read" in char.properties:
                            print("    readable")
                            data = await client.read_gatt_char(char.uuid)
                            print("    ",codecs.decode(data, 'UTF-8'))
                            
        except Exception as exc:
            print(traceback.format_exc())
            print(exc)

    print('attempt disconnect')    
    await client.disconnect()
        

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    #loop.run_until_complete(run(ADDRESS, True))


    