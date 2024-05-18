#!/usr/bin/env python

import time
import asyncio
import threading
from websockets.server import serve
from soil import SoilInfo, calculate_goodness
from data_grapher import update_plot, get_plot_data
from flask import Flask, request, jsonify, Response
import io

app = Flask(__name__)
books = [{'id': 1, 'title': 'Python Essentials', 'author': 'Jane Doe'}]


# routes for host:25565
@app.route('/plot', methods=['GET'])
def get_plot():
    return Response(get_plot_data(), mimetype='text/plain')


async def websocket_loop():
    async with serve(recv, "0.0.0.0", 9090):
        await asyncio.Future()  # run forever


async def recv(websocket):
    async for message in websocket:
        print(f"recieved message: {message}")
        soil_info: SoilInfo = SoilInfo(message)
        soil_goodness: float = calculate_goodness(soil_info)
        print(f"soil goodness: {soil_goodness}")
        print("plot updated...")
        update_plot(soil_info, soil_goodness)
        await websocket.send(f"soil goodness: {soil_goodness}")


async def main():
    # run websock loop and updates plot data
    t1 = threading.Thread(target=asyncio.run, args=(websocket_loop(),))
    t1.daemon = True
    t1.start()
    # run flask api
    app.run(host="0.0.0.0", port=25565)


asyncio.run(main())
