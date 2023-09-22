# https://getwavecake.com/blog/reading-your-phones-battery-level-over-bluetooth-ble-with-python-bleak/

import asyncio

from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(f'{d.name} -> {d.address}') # -> {d.details}')

asyncio.run(main())  
