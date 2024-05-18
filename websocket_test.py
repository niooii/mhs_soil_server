from websockets.sync.client import connect

def hello():
    with connect("ws://localhost:9090") as websocket:
        websocket.send("some test data fromclient")
        print(f"sent test data")

hello()
