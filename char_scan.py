#import bleak (https://pypi.org/project/bleak/)
"""
from here: https://github.com/hbldh/bleak/issues/157
"""

import asyncio
import logging
import traceback

from bleak import BleakClient

NOT_FOUND_LABEL = "NOT FOUND"
UNDEFINED_LABEL = "UNDEFINED"

address = NOT_FOUND_LABEL
uuid = UNDEFINED_LABEL
model = UNDEFINED_LABEL
bdate = UNDEFINED_LABEL 

async def run(address, debug=False):
    log = logging.getLogger(__name__)
    if debug:
        import sys

        loop.set_debug(True)
        log.setLevel(logging.DEBUG)
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(logging.DEBUG)
        log.addHandler(h)
        
    async with BleakClient(address) as client:
        x = await client.is_connected()
        log.info("Connected: {0}".format(x))
        print('...pairing')
        b_paired = await client.pair()
        print()
        print('...Reading Services')
        for service in client.services:
            log.info("[Service] {0}: {1}".format(service.uuid, service.description))
            for char in service.characteristics:
                characteristic = char
                try:
                    uuid = bytes(await client.read_gatt_char(char.uuid))
                except:
                    print(f'EXCEPTION:{traceback.format_exception}')

                properties = char.properties
                desc = char.description
                if "read" in char.properties:
                    try:
                        value = bytes(await client.read_gatt_char(char.uuid))
                        print(f"{char.description} - {char.uuid} -> {value}")
                    except Exception as e:
                        value = str(e).encode()
                else:
                    value = None
                log.info(
                    "\t[Characteristic] {0}: ({1}) | Name: {2}, Value: {3} ".format(
                        char.uuid, ",".join(char.properties), char.description, value
                    )
                )
                for descriptor in char.descriptors:
                    value = await client.read_gatt_descriptor(descriptor.handle)
                    log.info(
                        "\t\t[Descriptor] {0}: (Handle: {1}) | Value: {2} ".format(
                            descriptor.uuid, descriptor.handle, bytes(value)
                        )
                    )

        print('disconnecting')    
        await client.disconnect()

if __name__ == "__main__":
    address = ('ED:B9:4A:79:34:B4')
    loop = asyncio.get_event_loop()
    asyncio.run(run(address, True))