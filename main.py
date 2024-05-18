#!/usr/bin/env python

import time
import asyncio
import threading
from websockets.server import serve
from soil import SoilInfo, calculate_goodness
from data_grapher import update_plot
import matplotlib


def update_plot_loop():
    while True:
        time.sleep(0.5)
        update_plot()


async def echo(websocket):
    async for message in websocket:
        print(f"recieved message: {message}")
        soil_info: SoilInfo = SoilInfo(message)
        soil_goodness: float = calculate_goodness(soil_info)
        print(f"soil goodness: {soil_goodness}")
        await websocket.send(f"soil goodness: {soil_goodness}")


async def main():
    t1 = threading.Thread(target=update_plot, args=())
    t1.daemon = True
    t1.start()
    async with serve(echo, "0.0.0.0", 9090):
        await asyncio.Future()  # run forever


asyncio.run(main())




