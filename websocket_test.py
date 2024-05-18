from websockets.sync.client import connect
import time


def hello():
    coord_x: int = 0
    coord_y: int = 0
    with connect("ws://96.246.237.185:9090") as websocket:
        for n in range(0, 25):
            for k in range(0, 25):
                websocket.send(f"{coord_x},{coord_y}")
                message = websocket.recv()
                print(f"Received: {message}")
                time.sleep(0.5)
                coord_x += 1
            coord_x = 0
            coord_y += 1

hello()
