from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from websocket import create_connection

import json
import math
import re

from service import ArbitrageService

app = FastAPI()

arbitrage_handler = ArbitrageService()

# @app.on_event("startup")
# @repeat_every(seconds=5, wait_first=True)
# async def periodic():
#     try:
#         print(arbitrage_handler.handle(1))
#         # ws = create_connection("ws://socket:8000/ws?token=cron")
#         # ws.send("""{"to" : "1", "message" : "Hey."}""")
#         # ws.send("""{"to" : "2", "message" : "Hey Hey."}""")
#         # ws.close()
#     except Exception as e:
#         print(e)