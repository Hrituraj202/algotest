from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from database.query import query_get, query_put, query_update
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from user import Auth, SignInRequestModel, SignUpRequestModel, UserAuthResponseModel, UserUpdateRequestModel, UserResponseModel, register_user, signin_user, update_user, get_all_users, get_user_by_id
from trade import TradeUpdateRequestModel, TradeResponseModel, add_trade, get_all_trades, get_trade_by_id, get_trades_by_user_id

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from redis import Redis

import json

import traceback

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:4000",
    "http://localhost:19006"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()
auth_handler = Auth()

redis = Redis(host='redis')


###############################
########## Auth APIs ##########
###############################

@app.get('/')
def home():
    redis.incr('hits')
    print(redis.get('hits'))
    return JSONResponse(status_code=200, content={'msg': 'welcome to AlgoTest'})

@app.post('/v1/signup', response_model=UserAuthResponseModel)
def signup_api(user_details: SignUpRequestModel):
    """
    This sign-up API allow you to register your account, and return access token.
    """
    user = register_user(user_details)
    access_token = auth_handler.encode_token(user_details.email)
    refresh_token = auth_handler.encode_refresh_token(user_details.email)
    return JSONResponse(status_code=200, content={'token': {'access_token': access_token, 'refresh_token': refresh_token}, 'user': user})


@app.post('/v1/signin', response_model=UserAuthResponseModel)
def signin_api(user_details: SignInRequestModel):
    """
    This sign-in API allow you to obtain your access token.
    """
    user = signin_user(user_details.email, user_details.password)

    if not redis.exists('user:'+str(user['id'])):
        redis.hset('user:'+str(user['id']), mapping={
            "threshold": 1
        })
    # print(redis.hgetall('user:'+str(user['id'])))

    access_token = auth_handler.encode_token(user['email'])
    refresh_token = auth_handler.encode_refresh_token(user['email'])
    return JSONResponse(status_code=200, content={'token': {'access_token': access_token, 'refresh_token': refresh_token}, 'user': user})


@app.get('/v1/refresh-token')
def refresh_token_api(refresh_token: str):
    """
    This refresh-token API allow you to obtain new access token.
    """
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}


################################
########## Users APIs ##########
################################

@app.get("/v1/users", response_model=list[UserResponseModel])
def get_all_users_api(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    This users get API allow you to fetch all user data.
    """
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        user = get_all_users()
        return JSONResponse(status_code=200, content=jsonable_encoder(user))
    return JSONResponse(status_code=401, content={'error': 'Faild to authorize'})


@app.get("/v1/user/{user_id}", response_model=UserResponseModel)
def get_user_api(user_id: int, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    This user API allow you to fetch specific user data.
    """
    try:
        token = credentials.credentials
        if (auth_handler.decode_token(token)):
            user = get_user_by_id(user_id)
            return JSONResponse(status_code=200, content=jsonable_encoder(user))
        return JSONResponse(status_code=401, content={'error': 'Faild to authorize'})
    except Exception as e:
        print(traceback.format_exc())
        print("An exception occurred ", e)


@app.post("/v1/user/update", response_model=UserResponseModel)
def update_user_api(user_details: UserUpdateRequestModel, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    This user update API allow you to update user data.
    """
    token = credentials.credentials
    if (auth_handler.decode_token(token)):
        user = update_user(user_details)
        return JSONResponse(status_code=200, content=jsonable_encoder(user))
    return JSONResponse(status_code=401, content={'error': 'Faild to authorize'})

@app.post("/v1/user/{user_id}/trades", response_model=TradeResponseModel)
def create_trade_api(trade_details: TradeUpdateRequestModel):
    """
    This trade create API allow you to create trade data.
    """
    trade = add_trade(trade_details)
    return JSONResponse(status_code=200, content=jsonable_encoder(trade))

@app.get('/v1/user/{user_id}/trades', response_model=TradeResponseModel)
def get_user_trades(user_id: int, credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    This user API allow you to fetch specific user trade data.
    """
    try:
        token = credentials.credentials
        if (auth_handler.decode_token(token)):
            trades = get_trades_by_user_id(user_id)
            print(trades)
            return JSONResponse(status_code=200, content=jsonable_encoder(trades))
        return JSONResponse(status_code=401, content={'error': 'Faild to authorize'})
    except Exception as e:
        # print(traceback.format_exc())
        print("An exception occurred ", e)

###############################
########## Test APIs ##########
###############################

# @app.get('/secret')
# def secret_data_api(credentials: HTTPAuthorizationCredentials = Security(security)):
#     """
#     This secret API is just for testing. Need access token to access this API.
#     """
#     token = credentials.credentials
#     if (auth_handler.decode_token(token)):
#         return 'Top Secret data only authorized users can access this info'


# @app.get('/not-secret')
# def not_secret_data_api():
#     """
#     This not-secret API is just for testing.
#     """
#     return 'Not secret data'

# @app.get('/exchange/listings')
# def get_trades():

#     url = 'https://pro-api.coinmarketcap.com/v1/exchange/listings/latest'

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '0eae5252-5b66-46e0-81d3-93fa6080358f',
#     }

#     session = Session()
#     session.headers.update(headers)

#     parameters = {
#         # 'id' : 8670,
#         # 'slug' : "binance"
#     }

#     try:
#         response = session.get(url, params=parameters)
#         data = json.loads(response.text)
#         print(data)
#         return data
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)

# @app.get('/cryptocurrency/market-pairs')
# def get_trades():

#     url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/market-pairs/latest'

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '0eae5252-5b66-46e0-81d3-93fa6080358f',
#     }

#     session = Session()
#     session.headers.update(headers)

#     parameters = {
#         'id' : 9654,
#         # 'slug' : "binance"
#     }

#     try:
#         response = session.get(url, params=parameters)
#         data = json.loads(response.text)
#         print(data)
#         return data
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)

# @app.get('/exchange/assets')
# def get_trades():

#     url = 'https://pro-api.coinmarketcap.com/v1/exchange/assets'

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '0eae5252-5b66-46e0-81d3-93fa6080358f',
#     }

#     session = Session()
#     session.headers.update(headers)

#     parameters = {
#         'id' : 270,
#         # 'slug' : "binance"
#     }

#     try:
#         response = session.get(url, params=parameters)
#         data = json.loads(response.text)
#         print(data)
#         return data
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)

# @app.get('/exchange/map')
# def get_trades():

#     url = 'https://pro-api.coinmarketcap.com/v1/exchange/map'

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '0eae5252-5b66-46e0-81d3-93fa6080358f',
#     }

#     session = Session()
#     session.headers.update(headers)

#     parameters = {
#         # 'id' : 270,
#         # 'slug' : "binance"
#     }

#     try:
#         response = session.get(url, params=parameters)
#         data = json.loads(response.text)
#         print(data)
#         return data
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)

# @app.get('/cryptocurrency/listings')
# def get_trades():

#     url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': '0eae5252-5b66-46e0-81d3-93fa6080358f',
#     }

#     session = Session()
#     session.headers.update(headers)

#     parameters = {
#         # 'id' : 270,
#         # 'slug' : "binance"
#     }

#     try:
#         response = session.get(url, params=parameters)
#         data = json.loads(response.text)
#         print(data)
#         return data
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         print(e)

# @app.get('/test/{user_id}')
# def send_message(user_id: int):
#     return redis.hgetall('user:'+str(user_id))

# @app.get('/find_pairs')
# def find_pairs_optimized():

#     exchange_values = {
#         "Binance": 1800.5320387732727,
#         "Coinbase": 1800.5320387732727,
#         "Kraken": 1900.5320387732727,
#         "Bitfinex": 1500.5320387732727,
#         "Gemini": 1800.5320387732727
#     }
#     pairs = []
#     stack = []

#     # exchange_values.items() produce tuples
#     sorted_exchanges = sorted(exchange_values.items(), key=lambda item: item[1])

#     for (exchange, value) in sorted_exchanges:
#         while stack and exchange_values[stack[-1]] < value:
#             i = stack.pop()
#             pairs.append((i, exchange))

#         stack.append(exchange)

#     result_dict = {}
#     for pair in pairs:
#         value1 = exchange_values[pair[0]]
#         value2 = exchange_values[pair[1]]
#         key = f"{pair[0]},{pair[1]}"
#         result_dict[key] = f"{value1},{value2},{value2-value1}"

#     print(result_dict)

#     return 1


# @app.get('/solve_format')
# def solve_format():
#     input_data = {'ETH': {'Gemini,Binance': '1722,1800,78'}}

#     output_data = {}

#     for exchanges, prices in input_data['ETH'].items():
#         exchange_names = exchanges.split(',')
#         prices = prices.split(',')
        
#         for exchange, price in zip(exchange_names, prices):
#             output_data[exchange] = {
#                 "name": exchange,
#                 "currency": "ETH",
#                 "price": price
#             }

#     print(output_data)
#     return 1
