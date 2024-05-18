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

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)


# routes for host:25565
@app.route('/plot', methods=['GET'])
def get_plot():
    response = Response(get_plot_data())
    response.mimetype = 'text/plain'
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


time_since_last_read: float = time.time()


def arduino_read_loop():
    global time_since_last_read
    while True:
        # if time.time() - time_since_last_read < 0.1:
        #     continue
        data = arduino.readline()
        if len(data) == 0:
            continue
        message = data.decode('ascii')
        soil_info: SoilInfo = SoilInfo(message)
        soil_goodness: float = calculate_goodness(soil_info)
        print(f"soil goodness: {soil_goodness}")
        print("plot updated...")
        update_plot(soil_goodness, False)
        time_since_last_read = time.time()


async def main():
    update_plot(0, True)
    # run websock loop and updates plot data
    t1 = threading.Thread(target=arduino_read_loop, args=())
    t1.daemon = True
    t1.start()
    # run flask api
    app.run(host="0.0.0.0", port=25565)


asyncio.run(main())
