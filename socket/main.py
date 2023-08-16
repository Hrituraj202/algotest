from fastapi import FastAPI, WebSocket, WebSocketDisconnect, WebSocketException, Query, Depends
from typing import Annotated

import json
from redis import Redis

app = FastAPI()

redis = Redis(host='redis')

# clients = []
# initial stable version
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     clients.append(websocket)
#     print(*clients)
#     await websocket.accept()
#     while True:
#         try:
#             try:
#                 data = await websocket.receive_text()
#             except RuntimeError:
#                 break
#             # print(data)
#             for client in clients:
#                 if client != websocket:
#                     await client.send_text(f"{data}")
#         except WebSocketDisconnect:
#             clients.remove(websocket)

async def get_token(
    websocket: WebSocket,
    token: Annotated[str | None, Query()] = None,
):
    if token is None:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    return token

connections = {}

# async def broadcast(message: str, sender_token: str):
#     for token, connection in connections.items():
#         if token != sender_token:
#             await connection.send_text(message)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: Annotated[str, Depends(get_token)]):
    await websocket.accept()
    connections[token] = websocket
    try:
        while True:
            data = await websocket.receive_text()
            await handleRequest(json.loads(data), token)
    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if token in connections:
            del connections[token]

async def handleRequest(message, token):
    if(token == 'cron'):
        if message['to'] in connections:
            await connections[message['to']].send_text(message['message'])
    else:
        redis.hset('user:'+str(token), mapping={
            "threshold": message['message']
        })