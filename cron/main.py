from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from websocket import create_connection

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=30, wait_first=True)
async def periodic():
    ws = create_connection("ws://socket:8000/ws")
    ws.send("Hello, World")
    ws.close()
    print("hi")