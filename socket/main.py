from fastapi import FastAPI, WebSocket, WebSocketDisconnect
app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            # print(data)
            await websocket.send_text(f"{data}")
        except WebSocketDisconnect:
            pass