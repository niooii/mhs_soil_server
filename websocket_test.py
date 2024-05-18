from websockets.sync.client import connect

def hello():
    with connect("ws://96.246.237.185:9090") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        print(f"Received: {message}")

hello()
