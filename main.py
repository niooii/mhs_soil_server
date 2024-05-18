#!/usr/bin/env python

import time
import asyncio
import threading
from websockets.server import serve
from soil import SoilInfo, calculate_goodness
from data_grapher import update_plot, get_plot_data
from flask import Flask, request, jsonify, Response
import io
import serial

app = Flask(__name__)

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)

# routes for host:25565
@app.route('/plot', methods=['GET'])
def get_plot():
    return Response(get_plot_data(), mimetype='text/plain')


def arduino_read_loop():
    while True:
        time.sleep(0.2)
        data = arduino.readline()
        if len(data) == 0:
            continue
        message = data.decode('ascii')
        soil_info: SoilInfo = SoilInfo(message)
        soil_goodness: float = calculate_goodness(soil_info)
        print(f"soil goodness: {soil_goodness}")
        print("plot updated...")
        update_plot(soil_info, soil_goodness)


async def main():
    # run websock loop and updates plot data
    t1 = threading.Thread(target=arduino_read_loop, args=())
    t1.daemon = True
    t1.start()
    # run flask api
    app.run(host="0.0.0.0", port=25565)


asyncio.run(main())
