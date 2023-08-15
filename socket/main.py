from fastapi import FastAPI, WebSocket, WebSocketDisconnect
app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    clients.append(websocket)
    print(*clients)
    await websocket.accept()
    while True:
        try:
            try:
                data = await websocket.receive_text()
            except RuntimeError:
                break
            # print(data)
            for client in clients:
                if client != websocket:
                    await client.send_text(f"{data}")
        except WebSocketDisconnect:
            clients.remove(websocket)