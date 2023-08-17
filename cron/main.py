from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from websocket import create_connection

import json
import math
import re

from redis import Redis

from service import ArbitrageService, ApiService

app = FastAPI()
redis = Redis(host='redis')

arbitrage_handler = ArbitrageService()
api_handler = ApiService()

@app.on_event("startup")
@repeat_every(seconds=100, wait_first=True)
async def periodic():
    try:
        data = arbitrage_handler.handle(1)

        ws = create_connection("ws://socket:8000/ws?token=cron")

        for userKey in redis.keys('user:*'):

            user_id = userKey.decode('utf-8').split(':')[1]

            filteredData = arbitrage_handler.handleThreshold( data, redis.hgetall(userKey)[b'threshold'].decode('utf-8') )
            
            if len(filteredData) <= 2:
                continue

            #create trade
            api_handler.createTrade(user_id, filteredData)
            
            filteredData = json.dumps(filteredData)

            response = json.dumps({
                "to" : user_id,
                "message" : filteredData
            })

            ws.send(response)

        ws.close()
    except Exception as e:
        print(e)