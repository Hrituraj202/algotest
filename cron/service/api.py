import os
from fastapi import HTTPException  # used to handle error handling
from datetime import datetime, timedelta

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class ApiService():
    secret = os.getenv("API_SECRET_STRING")
    baseUrl = "https://pro-api.coinmarketcap.com"

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': secret,
    }

    session = Session()
    session.headers.update(headers)


    simulateTest = False

    def handle(self, exchange_id, simulateTest):
        try:
            if simulateTest:
                return self.testCallExchangeAssets(exchange_id)
            else:
                return self.callExchangeAssets(exchange_id)
        except Exception as e:
            print(e)

    def callExchangeAssets(self, exchange_id):
        parameters = {
            'id' : exchange_id
        }

        url = self.baseUrl + "/v1/exchange/assets"

        try:
            response = self.session.get(url, params=parameters)
            data = json.loads(response.text)
            print(data)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

    def testCallExchangeAssets(self, exchange_id):
        try:
            data = json.loads("""{
                                "status": {
                                    "timestamp": "2023-08-17T07:03:24.941Z",
                                    "error_code": 0,
                                    "error_message": null,
                                    "elapsed": 46,
                                    "credit_count": 1,
                                    "notice": null
                                },
                                "data": [
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 7000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3029,
                                            "price_usd": 0.36414956983259683,
                                            "symbol": "FLUX",
                                            "name": "Flux"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 329045,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8602,
                                            "price_usd": 4.742787859137861,
                                            "symbol": "AUCTION",
                                            "name": "Bounce Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 933139113.1,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4036,
                                            "price_usd": 0.004823400162785201,
                                            "symbol": "COS",
                                            "name": "Contentos"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 50000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6187,
                                            "price_usd": 0.04370694864880288,
                                            "symbol": "SRM",
                                            "name": "Serum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 40000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2071,
                                            "price_usd": 0.07214579105943983,
                                            "symbol": "REQ",
                                            "name": "Request"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 94031381.29,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 15678,
                                            "price_usd": 0.1399188119419297,
                                            "symbol": "VOXEL",
                                            "name": "Voxies"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 476.14,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 12551583.02,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7412,
                                            "price_usd": 0.23065466154410075,
                                            "symbol": "UFT",
                                            "name": "UniLend"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 20000000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2682,
                                            "price_usd": 0.0011887385609589988,
                                            "symbol": "HOT",
                                            "name": "Holo"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 6584149.57,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 2563507.03,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8000,
                                            "price_usd": 1.730340030241288,
                                            "symbol": "LDO",
                                            "name": "Lido DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 74072084,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6719,
                                            "price_usd": 0.09942367902316804,
                                            "symbol": "GRT",
                                            "name": "The Graph"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 27323000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1856,
                                            "price_usd": 0.025865068390137178,
                                            "symbol": "DNT",
                                            "name": "district0x"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 33241566.73,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6758,
                                            "price_usd": 0.6827393888036559,
                                            "symbol": "SUSHI",
                                            "name": "SushiSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9",
                                        "balance": 3999333220.56,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 16946168.49,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 16790000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5161,
                                            "price_usd": 0.10478848263414127,
                                            "symbol": "WRX",
                                            "name": "WazirX"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 1954171730023.56,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 9816,
                                            "price_usd": 3.1320477944691994e-07,
                                            "symbol": "NFT",
                                            "name": "APENFT"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 114686334.79,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8104,
                                            "price_usd": 0.26931518386189496,
                                            "symbol": "1INCH",
                                            "name": "1inch Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 4241314.07,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xacd03d601e5bb1b275bb94076ff46ed9d753435a",
                                        "balance": 6891175.26,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 11840,
                                            "price_usd": 1.4558134437345407,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 264908.47,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7672,
                                            "price_usd": 4.020318298953861,
                                            "symbol": "UNFI",
                                            "name": "Unifi Protocol DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 125093.89,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5034,
                                            "price_usd": 22.41090214899516,
                                            "symbol": "KSM",
                                            "name": "Kusama"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 46964.27,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5692,
                                            "price_usd": 47.02453637096567,
                                            "symbol": "COMP",
                                            "name": "Compound"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 6948515.7,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7046,
                                            "price_usd": 0.8447279420111978,
                                            "symbol": "GHST",
                                            "name": "Aavegotchi"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 3796339.42,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1697,
                                            "price_usd": 0.1874788142953606,
                                            "symbol": "BAT",
                                            "name": "Basic Attention Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 506748.27,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 109338612.47,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 17751,
                                            "price_usd": 0.021140537287923256,
                                            "symbol": "T",
                                            "name": "Threshold"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1xrfwzlu9c5208lhtn7ywt0mjrhjh4nt4fjyqxy",
                                        "balance": 11696.75,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1500000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2398,
                                            "price_usd": 0.004864649064665026,
                                            "symbol": "KEY",
                                            "name": "SelfKey"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 10101375.61,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6138,
                                            "price_usd": 0.23526694555057048,
                                            "symbol": "DIA",
                                            "name": "DIA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3843.83,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5864,
                                            "price_usd": 5781.231319319467,
                                            "symbol": "YFI",
                                            "name": "yearn.finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 10433124.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8255,
                                            "price_usd": 0.24411079426507706,
                                            "symbol": "PROS",
                                            "name": "Prosper"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 3650000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2682,
                                            "price_usd": 0.0011887385609589988,
                                            "symbol": "HOT",
                                            "name": "Holo"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 1792905.13,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6210,
                                            "price_usd": 0.360945325246123,
                                            "symbol": "SAND",
                                            "name": "The Sandbox"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 87000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2348,
                                            "price_usd": 0.04175809438375896,
                                            "symbol": "MDT",
                                            "name": "Measurable Data Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 8072794.75,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2071,
                                            "price_usd": 0.07214579105943983,
                                            "symbol": "REQ",
                                            "name": "Request"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13855,
                                            "price_usd": 8.344127675596797,
                                            "symbol": "ENS",
                                            "name": "Ethereum Name Service"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 92849196.4,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5026,
                                            "price_usd": 0.0587380061789854,
                                            "symbol": "OXT",
                                            "name": "Orchid"
                                        }
                                    },
                                    {
                                        "wallet_address": "3AeUiDpPPUrUBS377584sFCpx8KLfpX9Ry",
                                        "balance": 467.51,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 1901,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 10529,
                                            "price_usd": 0.005463450933392547,
                                            "symbol": "SUN",
                                            "name": "Sun (New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1389812.66,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1808,
                                            "price_usd": 0.516594969575573,
                                            "symbol": "OMG",
                                            "name": "OMG Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 4440721.92,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2424,
                                            "price_usd": 0.1968938943092629,
                                            "symbol": "AGIX",
                                            "name": "SingularityNET"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 75586466.48,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5691,
                                            "price_usd": 0.02430307560391889,
                                            "symbol": "SKL",
                                            "name": "SKALE"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 8805000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 44000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2424,
                                            "price_usd": 0.1968938943092629,
                                            "symbol": "AGIX",
                                            "name": "SingularityNET"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 26000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2132,
                                            "price_usd": 0.142382210141333,
                                            "symbol": "POWR",
                                            "name": "Powerledger"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xeae7380dd4cef6fbd1144f49e4d1e6964258a4f4",
                                        "balance": 3668276.44,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 25186266110.15,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2682,
                                            "price_usd": 0.0011887385609589988,
                                            "symbol": "HOT",
                                            "name": "Holo"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 187920.04,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8719,
                                            "price_usd": 49.182340809909334,
                                            "symbol": "ILV",
                                            "name": "Illuvium"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 43025253923695.45,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5994,
                                            "price_usd": 9.265611730463855e-06,
                                            "symbol": "SHIB",
                                            "name": "Shiba Inu"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 12000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5690,
                                            "price_usd": 1.5999326532552023,
                                            "symbol": "RNDR",
                                            "name": "Render"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 1542065.51,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 9481,
                                            "price_usd": 0.6005570479763356,
                                            "symbol": "PENDLE",
                                            "name": "Pendle"
                                        }
                                    },
                                    {
                                        "wallet_address": "TNXoiAJ3dct8Fjg4M9fkLFh9S2v9TXc32G",
                                        "balance": 137304587.6,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 1000000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1m5amny2gs3xdyta6pksmr43zu4727w24syyks7",
                                        "balance": 13162.92,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 86733988.35,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2212,
                                            "price_usd": 0.01020141951654088,
                                            "symbol": "QSP",
                                            "name": "Quantstamp"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 27000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "DRweGdMgohChLBn2TamjCNicKYEncRgj5a",
                                        "balance": 286296208.64,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "DGiYKUGbzRtppwdoinym7ZJXWuBqBuHxUk",
                                        "balance": 151605154.01,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 26342701.57,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11568,
                                            "price_usd": 0.5506115151550748,
                                            "symbol": "AGLD",
                                            "name": "Adventure Gold"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1528037.79,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3640,
                                            "price_usd": 7.005585781859719,
                                            "symbol": "LPT",
                                            "name": "Livepeer"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3241781.48,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 6048338.85,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 22461,
                                            "price_usd": 0.34575179462685857,
                                            "symbol": "HFT",
                                            "name": "Hashflow"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 41483853.46,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 83679.97,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3194038.15,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5617,
                                            "price_usd": 1.4942992899842977,
                                            "symbol": "UMA",
                                            "name": "UMA"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 131801764.24,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5161,
                                            "price_usd": 0.10478848263414127,
                                            "symbol": "WRX",
                                            "name": "WazirX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 344000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2143,
                                            "price_usd": 0.022284337066153518,
                                            "symbol": "DATA",
                                            "name": "Streamr"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x3c783c21a0383057d128bae431894a5c19f9cf06",
                                        "balance": 13570.38,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 357798,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 11857,
                                            "price_usd": 39.973107150982095,
                                            "symbol": "GMX",
                                            "name": "GMX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 1545440.12,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6210,
                                            "price_usd": 0.360945325246123,
                                            "symbol": "SAND",
                                            "name": "The Sandbox"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 14000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3773,
                                            "price_usd": 0.19884966503504237,
                                            "symbol": "FET",
                                            "name": "Fetch.ai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 86500000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4118,
                                            "price_usd": 0.018444818081190584,
                                            "symbol": "FOR",
                                            "name": "ForTube"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 2860714.29,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7429,
                                            "price_usd": 0.8791895148928164,
                                            "symbol": "LQTY",
                                            "name": "Liquity"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 5545427.12,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1768,
                                            "price_usd": 0.1320025472407208,
                                            "symbol": "ADX",
                                            "name": "AdEx"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 56,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6941,
                                            "price_usd": 28556.88223868612,
                                            "symbol": "HBTC",
                                            "name": "Huobi BTC"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 535029.2,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5692,
                                            "price_usd": 47.02453637096567,
                                            "symbol": "COMP",
                                            "name": "Compound"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 30000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7224,
                                            "price_usd": 0.10730965957273395,
                                            "symbol": "DODO",
                                            "name": "DODO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 6751919.38,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2638,
                                            "price_usd": 0.13334262776078043,
                                            "symbol": "CTXC",
                                            "name": "Cortex"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 933148.77,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 105351628.09,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6210,
                                            "price_usd": 0.360945325246123,
                                            "symbol": "SAND",
                                            "name": "The Sandbox"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 125122.19,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1552,
                                            "price_usd": 17.25275174846124,
                                            "symbol": "MLN",
                                            "name": "Enzyme"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 25299211.35,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6187,
                                            "price_usd": 0.04370694864880288,
                                            "symbol": "SRM",
                                            "name": "Serum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
                                        "balance": 351970.21,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 6700,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5957,
                                            "price_usd": 498.8818395517828,
                                            "symbol": "YFII",
                                            "name": "DFI.Money"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9f8c163cba728e99993abe7495f06c0a3c8ac8b9",
                                        "balance": 309146,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 5805,
                                            "price_usd": 11.449580596258247,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 828325.41,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4943,
                                            "price_usd": 1.0000341428418609,
                                            "symbol": "DAI",
                                            "name": "Dai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 189561642.74,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 161715,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 127000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7224,
                                            "price_usd": 0.10730965957273395,
                                            "symbol": "DODO",
                                            "name": "DODO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 3341794.03,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 18112,
                                            "price_usd": 1.9139383408032802,
                                            "symbol": "ALPINE",
                                            "name": "Alpine F1 Team Fan Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 538511511.45,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5007,
                                            "price_usd": 0.002362212928749703,
                                            "symbol": "TROY",
                                            "name": "TROY"
                                        }
                                    },
                                    {
                                        "wallet_address": "395vnFScKQ1ay695C6v7gf89UzoFpx3WuJ",
                                        "balance": 1758.53,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 1851176578.8,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4036,
                                            "price_usd": 0.004823400162785201,
                                            "symbol": "COS",
                                            "name": "Contentos"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 48663.72,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 12999,
                                            "price_usd": 16.11246853293979,
                                            "symbol": "SSV",
                                            "name": "ssv.network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe7804c37c13166ff0b37f5ae0bb07a3aebb6e245",
                                        "balance": 4574893.54,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1400000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8602,
                                            "price_usd": 4.742787859137861,
                                            "symbol": "AUCTION",
                                            "name": "Bounce Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 235511930.52,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 17751,
                                            "price_usd": 0.021140537287923256,
                                            "symbol": "T",
                                            "name": "Threshold"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 334.27,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3717,
                                            "price_usd": 28617.101745242293,
                                            "symbol": "WBTC",
                                            "name": "Wrapped Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 70000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5939,
                                            "price_usd": 30.63201654970751,
                                            "symbol": "WNXM",
                                            "name": "Wrapped NXM"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe2fc31f816a9b94326492132018c3aecc4a93ae1",
                                        "balance": 16363.51,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 41797017.27,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3992,
                                            "price_usd": 0.044512810351528924,
                                            "symbol": "COTI",
                                            "name": "COTI"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 39727670.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 17751,
                                            "price_usd": 0.021140537287923256,
                                            "symbol": "T",
                                            "name": "Threshold"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 207127,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 11857,
                                            "price_usd": 39.973107150982095,
                                            "symbol": "GMX",
                                            "name": "GMX"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 169400,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6636,
                                            "price_usd": 4.748201361456647,
                                            "symbol": "DOT",
                                            "name": "Polkadot"
                                        }
                                    },
                                    {
                                        "wallet_address": "3HdGoUTbcztBnS7UzY4vSPYhwr424CiWAA",
                                        "balance": 1999.92,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 13051094.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1925,
                                            "price_usd": 0.15321586396395542,
                                            "symbol": "WTC",
                                            "name": "Waltonchain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 31052145.36,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1856,
                                            "price_usd": 0.025865068390137178,
                                            "symbol": "DNT",
                                            "name": "district0x"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 291395.12,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2586,
                                            "price_usd": 2.321664881332331,
                                            "symbol": "SNX",
                                            "name": "Synthetix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 114890252.21,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2019,
                                            "price_usd": 0.04386865599482222,
                                            "symbol": "VIB",
                                            "name": "Viberate"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 120000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5117,
                                            "price_usd": 0.08502813254722748,
                                            "symbol": "OGN",
                                            "name": "Origin Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 18996311.38,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18037,
                                            "price_usd": 0.23378068221563175,
                                            "symbol": "MAV",
                                            "name": "Maverick Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 71748360.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7455,
                                            "price_usd": 0.17083954103778173,
                                            "symbol": "AUDIO",
                                            "name": "Audius"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 627471.96,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1788,
                                            "price_usd": 1.1649219812892724,
                                            "symbol": "MTL",
                                            "name": "Metal DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1070814.15,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 1711471.05,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6538,
                                            "price_usd": 0.5468384145822828,
                                            "symbol": "CRV",
                                            "name": "Curve DAO Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "3JFJPpH8Chwo7CDbyYQ4XcfgcjEP1FGRMJ",
                                        "balance": 193.95,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 6348224.61,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3330,
                                            "price_usd": 0.9984126185924139,
                                            "symbol": "USDP",
                                            "name": "Pax Dollar"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1079889675.32,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 14806,
                                            "price_usd": 0.010905799626187403,
                                            "symbol": "PEOPLE",
                                            "name": "ConstitutionDAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4039,
                                            "price_usd": 0.04687375470683488,
                                            "symbol": "ARPA",
                                            "name": "ARPA"
                                        }
                                    },
                                    {
                                        "wallet_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
                                        "balance": 562511100.23,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "DD1h9ojoyAdAGLXaqgqZP3j86AtxZs6jCn",
                                        "balance": 176644459.47,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 10090491.29,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6950,
                                            "price_usd": 0.47690763728000146,
                                            "symbol": "PERP",
                                            "name": "Perpetual Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 598186.56,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6636,
                                            "price_usd": 4.748201361456647,
                                            "symbol": "DOT",
                                            "name": "Polkadot"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 1159784,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 637520.5,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8536,
                                            "price_usd": 3.06261767866833,
                                            "symbol": "MASK",
                                            "name": "Mask Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 18823765.39,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7232,
                                            "price_usd": 0.093268266851401,
                                            "symbol": "ALPHA",
                                            "name": "Stella"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3602532.99,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 17145,
                                            "price_usd": 0.21967647440195656,
                                            "symbol": "LOKA",
                                            "name": "League of Kingdoms Arena"
                                        }
                                    },
                                    {
                                        "wallet_address": "36zSLdRv1jyewjaC12fqK5fptn7PqewunL",
                                        "balance": 10031.96,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 3328601.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7226,
                                            "price_usd": 7.206011020391402,
                                            "symbol": "INJ",
                                            "name": "Injective"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 161452077.09,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4039,
                                            "price_usd": 0.04687375470683488,
                                            "symbol": "ARPA",
                                            "name": "ARPA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 114478932.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1966,
                                            "price_usd": 0.33374694855015846,
                                            "symbol": "MANA",
                                            "name": "Decentraland"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 13250.25,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1659,
                                            "price_usd": 107.5888548181615,
                                            "symbol": "GNO",
                                            "name": "Gnosis"
                                        }
                                    },
                                    {
                                        "wallet_address": "D7bg2iUG3UiHuTWjRqcjdJiEjHrsFASsjw",
                                        "balance": 1681615534.63,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 24730669.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1217218.2,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1788,
                                            "price_usd": 1.1649219812892724,
                                            "symbol": "MTL",
                                            "name": "Metal DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xF977814e90dA44bFA03b6295A0616a897441aceC",
                                        "balance": 955308.34,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 9360000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5893,
                                            "price_usd": 0.16095017532766467,
                                            "symbol": "FRONT",
                                            "name": "Frontier"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 75000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8037,
                                            "price_usd": 0.023066185882791315,
                                            "symbol": "TVK",
                                            "name": "Virtua"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 29392.01,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5692,
                                            "price_usd": 47.02453637096567,
                                            "symbol": "COMP",
                                            "name": "Compound"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 2115611.21,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 14783,
                                            "price_usd": 0.6777151316478582,
                                            "symbol": "MAGIC",
                                            "name": "MAGIC"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 622988.58,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7672,
                                            "price_usd": 4.020318298953861,
                                            "symbol": "UNFI",
                                            "name": "Unifi Protocol DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 19449.3,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 9860000,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 7461,
                                            "price_usd": 0.18848328059524438,
                                            "symbol": "PLA",
                                            "name": "PlayDapp"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 3417500730.46,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11289,
                                            "price_usd": 0.0004193090800843014,
                                            "symbol": "SPELL",
                                            "name": "Spell Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 315169622.45,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3964,
                                            "price_usd": 0.0020113234294809185,
                                            "symbol": "RSR",
                                            "name": "Reserve Rights"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3210547.38,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2130,
                                            "price_usd": 0.26374312786015564,
                                            "symbol": "ENJ",
                                            "name": "Enjin Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 200000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2840,
                                            "price_usd": 0.008262332833125429,
                                            "symbol": "QKC",
                                            "name": "QuarkChain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 8425000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8766,
                                            "price_usd": 0.8523112173510031,
                                            "symbol": "ALICE",
                                            "name": "MyNeighborAlice"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 53310792.83,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4758,
                                            "price_usd": 0.03516759240184835,
                                            "symbol": "DF",
                                            "name": "dForce"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 26887236.65,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 52,
                                            "price_usd": 0.5878633783129905,
                                            "symbol": "XRP",
                                            "name": "XRP"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1000007.43,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 25236735,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2588,
                                            "price_usd": 0.04179528411700283,
                                            "symbol": "LOOM",
                                            "name": "Loom Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "DE5opaXjFgDhFBqL6tBDxTAQ56zkX6EToX",
                                        "balance": 7259202272.47,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 195364434.42,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7080,
                                            "price_usd": 0.02084554777171437,
                                            "symbol": "GALA",
                                            "name": "Gala"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 12413330.03,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1637,
                                            "price_usd": 1.1341860890318043,
                                            "symbol": "RLC",
                                            "name": "iExec RLC"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 8328601,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3029,
                                            "price_usd": 0.36414956983259683,
                                            "symbol": "FLUX",
                                            "name": "Flux"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 9300000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7087,
                                            "price_usd": 1.421050310713961,
                                            "symbol": "DEGO",
                                            "name": "Dego Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 896405.14,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6833,
                                            "price_usd": 0.6277856656093501,
                                            "symbol": "LIT",
                                            "name": "Litentry"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 47239127.08,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11156,
                                            "price_usd": 2.0188445185052615,
                                            "symbol": "DYDX",
                                            "name": "dYdX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 4285734.51,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 5273604.59,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2780,
                                            "price_usd": 0.09735616019240688,
                                            "symbol": "NKN",
                                            "name": "NKN"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 177477.83,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6783,
                                            "price_usd": 5.351594584639869,
                                            "symbol": "AXS",
                                            "name": "Axie Infinity"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 23570000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2299,
                                            "price_usd": 0.30015180245867384,
                                            "symbol": "ELF",
                                            "name": "aelf"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 220846.53,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 5900000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7064,
                                            "price_usd": 0.11007672328851463,
                                            "symbol": "BAKE",
                                            "name": "BakeryToken"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 1223177488.33,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 3500,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 21829,
                                            "price_usd": 3068.1279185514745,
                                            "symbol": "TBC",
                                            "name": "Ten Best Coins"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 6380275.38,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13523,
                                            "price_usd": 0.3231218706388867,
                                            "symbol": "MC",
                                            "name": "Merit Circle"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 321632932.27,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4006,
                                            "price_usd": 0.04220216544088124,
                                            "symbol": "STPT",
                                            "name": "STP"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 10018017.08,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6758,
                                            "price_usd": 0.6827393888036559,
                                            "symbol": "SUSHI",
                                            "name": "SushiSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 1602000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 14052,
                                            "price_usd": 2.0464997001910703,
                                            "symbol": "PORTO",
                                            "name": "FC Porto Fan Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 830971.92,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 21763,
                                            "price_usd": 1.0027977762539162,
                                            "symbol": "USDTE",
                                            "name": "Tether Avalanche Bridged"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 18000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4092,
                                            "price_usd": 0.11765989588608315,
                                            "symbol": "DUSK",
                                            "name": "Dusk"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 1347985905,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2398,
                                            "price_usd": 0.004864649064665026,
                                            "symbol": "KEY",
                                            "name": "SelfKey"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4160000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8255,
                                            "price_usd": 0.24411079426507706,
                                            "symbol": "PROS",
                                            "name": "Prosper"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 33265419.02,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13523,
                                            "price_usd": 0.3231218706388867,
                                            "symbol": "MC",
                                            "name": "Merit Circle"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdccf3b77da55107280bd850ea519df3705d1a75a",
                                        "balance": 15693.87,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 1169465332698.84,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 24478,
                                            "price_usd": 1.2043396244619398e-06,
                                            "symbol": "PEPE",
                                            "name": "Pepe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9696f59e4d72e237be84ffd425dcad154bf96976",
                                        "balance": 52117161.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xF977814e90dA44bFA03b6295A0616a897441aceC",
                                        "balance": 10343842,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 2586,
                                            "price_usd": 2.321664881332331,
                                            "symbol": "SNX",
                                            "name": "Synthetix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 184642862.36,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "DJRaDXkewtLgwL9EZyTkWQEsxuyBUaveKU",
                                        "balance": 81396089,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 69810101.84,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3783,
                                            "price_usd": 0.021526053031444267,
                                            "symbol": "ANKR",
                                            "name": "Ankr"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
                                        "balance": 1133449.35,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 22764,
                                            "price_usd": 0.8548296835702033,
                                            "symbol": "HOOK",
                                            "name": "Hooked Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 55400.1,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 11857,
                                            "price_usd": 39.973107150982095,
                                            "symbol": "GMX",
                                            "name": "GMX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 30575917.78,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 23037,
                                            "price_usd": 0.3614706657835475,
                                            "symbol": "HIFI",
                                            "name": "Hifi Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 940000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7326,
                                            "price_usd": 2.2206543236327962,
                                            "symbol": "DEXE",
                                            "name": "DeXe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 328246137.61,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 22710,
                                            "price_usd": 0.01973121187905417,
                                            "symbol": "VIDT",
                                            "name": "VIDT DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 273908.83,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8536,
                                            "price_usd": 3.06261767866833,
                                            "symbol": "MASK",
                                            "name": "Mask Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 858369.07,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18876,
                                            "price_usd": 1.7887230786187478,
                                            "symbol": "APE",
                                            "name": "ApeCoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 18000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2416,
                                            "price_usd": 0.6840080701484711,
                                            "symbol": "THETA",
                                            "name": "Theta Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 97930037.79,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8487,
                                            "price_usd": 0.02911780030718518,
                                            "symbol": "TBCC",
                                            "name": "TBCC"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9f8c163cba728e99993abe7495f06c0a3c8ac8b9",
                                        "balance": 44791288.92,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 20492951.32,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 4943,
                                            "price_usd": 1.0000341428418609,
                                            "symbol": "DAI",
                                            "name": "Dai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 39000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4293,
                                            "price_usd": 0.015307579029299854,
                                            "symbol": "PERL",
                                            "name": "PERL.eco"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 758.28,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2396,
                                            "price_usd": 1799.7166400864119,
                                            "symbol": "WETH",
                                            "name": "WETH"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3043278.09,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 12999,
                                            "price_usd": 16.11246853293979,
                                            "symbol": "SSV",
                                            "name": "ssv.network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 2504086.81,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9421,
                                            "price_usd": 2.7300840325097386,
                                            "symbol": "FORTH",
                                            "name": "Ampleforth Governance Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 20000000,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 34701036.94,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1697,
                                            "price_usd": 0.1874788142953606,
                                            "symbol": "BAT",
                                            "name": "Basic Attention Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 900000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4066,
                                            "price_usd": 0.06881139785105253,
                                            "symbol": "CHZ",
                                            "name": "Chiliz"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 24000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2539,
                                            "price_usd": 0.05087587635660903,
                                            "symbol": "REN",
                                            "name": "Ren"
                                        }
                                    },
                                    {
                                        "wallet_address": "MWGTiJBNEQSfxTCrdC2VKEa55Lck27wr67",
                                        "balance": 8413.2,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x73f5ebe90f27b46ea12e5795d16c4b408b19cc6f",
                                        "balance": 13097.3,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 7828182.7,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1772,
                                            "price_usd": 0.2534620883650551,
                                            "symbol": "STORJ",
                                            "name": "Storj"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 135288746.99,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3978,
                                            "price_usd": 0.10505888189769066,
                                            "symbol": "CHR",
                                            "name": "Chromia"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 145573721.32,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6536,
                                            "price_usd": 0.02048071709252483,
                                            "symbol": "OM",
                                            "name": "MANTRA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 49456865.96,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8384,
                                            "price_usd": 0.03482302133831626,
                                            "symbol": "CLV",
                                            "name": "CLV"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 10180677.16,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 14556,
                                            "price_usd": 0.1305499752153701,
                                            "symbol": "BOBA",
                                            "name": "Boba Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe7804c37c13166ff0b37f5ae0bb07a3aebb6e245",
                                        "balance": 1037033.57,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 4943,
                                            "price_usd": 1.0000341428418609,
                                            "symbol": "DAI",
                                            "name": "Dai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe2fc31f816a9b94326492132018c3aecc4a93ae1",
                                        "balance": 13060102.68,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 10746,
                                            "price_usd": 0.07426541351824369,
                                            "symbol": "BSW",
                                            "name": "Biswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 270000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7725,
                                            "price_usd": 0.03422768065547463,
                                            "symbol": "TRU",
                                            "name": "TrueFi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 136000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3814,
                                            "price_usd": 0.012595021044361457,
                                            "symbol": "CELR",
                                            "name": "Celer Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 116427408.09,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10688,
                                            "price_usd": 0.2624587816246438,
                                            "symbol": "YGG",
                                            "name": "Yield Guild Games"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 43500000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4006,
                                            "price_usd": 0.04220216544088124,
                                            "symbol": "STPT",
                                            "name": "STP"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 217887.61,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2586,
                                            "price_usd": 2.321664881332331,
                                            "symbol": "SNX",
                                            "name": "Synthetix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 20511500.88,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18876,
                                            "price_usd": 1.7887230786187478,
                                            "symbol": "APE",
                                            "name": "ApeCoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 259438.45,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3155,
                                            "price_usd": 99.94682316783275,
                                            "symbol": "QNT",
                                            "name": "Quant"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 1091.6,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 355506.98,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 200810.69,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9308,
                                            "price_usd": 3.2036894083443537,
                                            "symbol": "PYR",
                                            "name": "Vulcan Forged PYR"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 100000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1732,
                                            "price_usd": 12.227137425133947,
                                            "symbol": "NMR",
                                            "name": "Numeraire"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 398000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4293,
                                            "price_usd": 0.015307579029299854,
                                            "symbol": "PERL",
                                            "name": "PERL.eco"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 80841.18,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6953,
                                            "price_usd": 6.527456357216569,
                                            "symbol": "FXS",
                                            "name": "Frax Share"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 75000225270863.12,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 16086,
                                            "price_usd": 4.4286497986976614e-07,
                                            "symbol": "BTT",
                                            "name": "BitTorrent(New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 90000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1966,
                                            "price_usd": 0.33374694855015846,
                                            "symbol": "MANA",
                                            "name": "Decentraland"
                                        }
                                    },
                                    {
                                        "wallet_address": "TQrY8tryqsYVCYS3MFbtffiPp2ccyn4STm",
                                        "balance": 192325123.76,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 6215921.4,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 13523,
                                            "price_usd": 0.3231218706388867,
                                            "symbol": "MC",
                                            "name": "Merit Circle"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 48000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3714,
                                            "price_usd": 0.05945232953471845,
                                            "symbol": "LTO",
                                            "name": "LTO Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 6594.91,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3155,
                                            "price_usd": 99.94682316783275,
                                            "symbol": "QNT",
                                            "name": "Quant"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 18000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2058,
                                            "price_usd": 0.09245317298578626,
                                            "symbol": "AST",
                                            "name": "AirSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 57266,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5692,
                                            "price_usd": 47.02453637096567,
                                            "symbol": "COMP",
                                            "name": "Compound"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 142315.4,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4120,
                                            "price_usd": 3.9668892439470778,
                                            "symbol": "PROM",
                                            "name": "Prom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3783,
                                            "price_usd": 0.021526053031444267,
                                            "symbol": "ANKR",
                                            "name": "Ankr"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 21000.08,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4150000.01,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9148,
                                            "price_usd": 0.2417256834697115,
                                            "symbol": "DREP",
                                            "name": "Drep [new]"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 20420992.47,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 628839.01,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xacd03d601e5bb1b275bb94076ff46ed9d753435a",
                                        "balance": 350020.94,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 2586,
                                            "price_usd": 2.321664881332331,
                                            "symbol": "SNX",
                                            "name": "Synthetix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 90983603,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6536,
                                            "price_usd": 0.02048071709252483,
                                            "symbol": "OM",
                                            "name": "MANTRA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 76000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6538,
                                            "price_usd": 0.5468384145822828,
                                            "symbol": "CRV",
                                            "name": "Curve DAO Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 8469.3,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7311,
                                            "price_usd": 285.34391276060694,
                                            "symbol": "BIFI",
                                            "name": "Beefy"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 53045985.67,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1496329.16,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10603,
                                            "price_usd": 0.6406360524384285,
                                            "symbol": "IMX",
                                            "name": "Immutable"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 8849489.65,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8104,
                                            "price_usd": 0.26931518386189496,
                                            "symbol": "1INCH",
                                            "name": "1inch Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 592508148.72,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3814,
                                            "price_usd": 0.012595021044361457,
                                            "symbol": "CELR",
                                            "name": "Celer Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJCo98saj6WND61g1uuKwJ9GMWMT9WkJFo",
                                        "balance": 200000000,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 597525.25,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18876,
                                            "price_usd": 1.7887230786187478,
                                            "symbol": "APE",
                                            "name": "ApeCoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 192563096307.59,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5994,
                                            "price_usd": 9.265611730463855e-06,
                                            "symbol": "SHIB",
                                            "name": "Shiba Inu"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 179923288,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2297,
                                            "price_usd": 0.00562276001714886,
                                            "symbol": "STMX",
                                            "name": "StormX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 29537194091.2,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 19924,
                                            "price_usd": 0.00019609914326139955,
                                            "symbol": "EPX",
                                            "name": "Ellipsis"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 55625.84,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 652399406.91,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7497,
                                            "price_usd": 0.008297742252965251,
                                            "symbol": "POND",
                                            "name": "Marlin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 194404697.15,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7064,
                                            "price_usd": 0.11007672328851463,
                                            "symbol": "BAKE",
                                            "name": "BakeryToken"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 70000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3978,
                                            "price_usd": 0.10505888189769066,
                                            "symbol": "CHR",
                                            "name": "Chromia"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 8836072.48,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8290,
                                            "price_usd": 0.08842556946970717,
                                            "symbol": "SUPER",
                                            "name": "SuperVerse"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7080,
                                            "price_usd": 0.02084554777171437,
                                            "symbol": "GALA",
                                            "name": "Gala"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 440000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7102,
                                            "price_usd": 0.012960554065743457,
                                            "symbol": "LINA",
                                            "name": "Linear Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 5059395.01,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 18112,
                                            "price_usd": 1.9139383408032802,
                                            "symbol": "ALPINE",
                                            "name": "Alpine F1 Team Fan Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 221091.75,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2943,
                                            "price_usd": 27.126028955566134,
                                            "symbol": "RPL",
                                            "name": "Rocket Pool"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1255796156.96,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7102,
                                            "price_usd": 0.012960554065743457,
                                            "symbol": "LINA",
                                            "name": "Linear Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 27100368.94,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4039,
                                            "price_usd": 0.04687375470683488,
                                            "symbol": "ARPA",
                                            "name": "ARPA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x56eddb7aa87536c09ccc2793473599fd21a8b17f",
                                        "balance": 37038105.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 1996008.36,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 500,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5864,
                                            "price_usd": 5781.231319319467,
                                            "symbol": "YFI",
                                            "name": "yearn.finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 47000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 22461,
                                            "price_usd": 0.34575179462685857,
                                            "symbol": "HFT",
                                            "name": "Hashflow"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 265850303.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 354.18,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4705,
                                            "price_usd": 1894.3189653673944,
                                            "symbol": "PAXG",
                                            "name": "PAX Gold"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 3523860,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1934,
                                            "price_usd": 0.20263980290989594,
                                            "symbol": "LRC",
                                            "name": "Loopring"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 9410383.65,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11232,
                                            "price_usd": 1.2193794399481575,
                                            "symbol": "HIGH",
                                            "name": "Highstreet"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 150000000,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 19966,
                                            "price_usd": 0.04303152915187717,
                                            "symbol": "QUICK",
                                            "name": "Quickswap [New]"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
                                        "balance": 3287.08,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1831,
                                            "price_usd": 210.29189810012312,
                                            "symbol": "BCH",
                                            "name": "Bitcoin Cash"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 353230.13,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5690,
                                            "price_usd": 1.5999326532552023,
                                            "symbol": "RNDR",
                                            "name": "Render"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 137054567.45,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 9020,
                                            "price_usd": 0.23502965647381124,
                                            "symbol": "TKO",
                                            "name": "Toko Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 283376697.98,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 18101,
                                            "price_usd": 0.0027175004180211427,
                                            "symbol": "NBT",
                                            "name": "NanoByte Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 200740941.24,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 77346867.41,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 20949,
                                            "price_usd": 0.0074591383012957806,
                                            "symbol": "OGV",
                                            "name": "Origin Dollar Governance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 9346.87,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1659,
                                            "price_usd": 107.5888548181615,
                                            "symbol": "GNO",
                                            "name": "Gnosis"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 3404405.32,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1925,
                                            "price_usd": 0.15321586396395542,
                                            "symbol": "WTC",
                                            "name": "Waltonchain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 461575.82,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8536,
                                            "price_usd": 3.06261767866833,
                                            "symbol": "MASK",
                                            "name": "Mask Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 25978715.57,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8335,
                                            "price_usd": 0.061195090594851946,
                                            "symbol": "MDX",
                                            "name": "Mdex"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 93171577.49,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8290,
                                            "price_usd": 0.08842556946970717,
                                            "symbol": "SUPER",
                                            "name": "SuperVerse"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 1406790.65,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6538,
                                            "price_usd": 0.5468384145822828,
                                            "symbol": "CRV",
                                            "name": "Curve DAO Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9f8c163cba728e99993abe7495f06c0a3c8ac8b9",
                                        "balance": 4290003.28,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 11396,
                                            "price_usd": 0.2609301853967535,
                                            "symbol": "JOE",
                                            "name": "JOE"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 35860843.4,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4118,
                                            "price_usd": 0.018444818081190584,
                                            "symbol": "FOR",
                                            "name": "ForTube"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 12662386.63,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 107525106.88,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5964,
                                            "price_usd": 0.8790661478570492,
                                            "symbol": "TWT",
                                            "name": "Trust Wallet Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 519411.14,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 7341195.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7208,
                                            "price_usd": 0.27198040279636876,
                                            "symbol": "POLS",
                                            "name": "Polkastarter"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 156911079.38,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8384,
                                            "price_usd": 0.03482302133831626,
                                            "symbol": "CLV",
                                            "name": "CLV"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 406031.04,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6193,
                                            "price_usd": 12.281319852245284,
                                            "symbol": "CREAM",
                                            "name": "Cream Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 8024972.64,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8615,
                                            "price_usd": 1.5140707102944173,
                                            "symbol": "ERN",
                                            "name": "Ethernity"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 170000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4118,
                                            "price_usd": 0.018444818081190584,
                                            "symbol": "FOR",
                                            "name": "ForTube"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 20839284.37,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2505,
                                            "price_usd": 0.09280251123591385,
                                            "symbol": "BLZ",
                                            "name": "Bluzelle"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 22801375.4,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 11396,
                                            "price_usd": 0.2609301853967535,
                                            "symbol": "JOE",
                                            "name": "JOE"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 95615027.8,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5161,
                                            "price_usd": 0.10478848263414127,
                                            "symbol": "WRX",
                                            "name": "WazirX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 8317843.17,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1788,
                                            "price_usd": 1.1649219812892724,
                                            "symbol": "MTL",
                                            "name": "Metal DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 4174524.59,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18037,
                                            "price_usd": 0.23378068221563175,
                                            "symbol": "MAV",
                                            "name": "Maverick Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 6000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1637,
                                            "price_usd": 1.1341860890318043,
                                            "symbol": "RLC",
                                            "name": "iExec RLC"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x082489a616ab4d46d1947ee3f912e080815b08da",
                                        "balance": 1029631.78,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 16613.23,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4248700.83,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7046,
                                            "price_usd": 0.8447279420111978,
                                            "symbol": "GHST",
                                            "name": "Aavegotchi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 21256214.62,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1808,
                                            "price_usd": 0.516594969575573,
                                            "symbol": "OMG",
                                            "name": "OMG Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 427774,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4944,
                                            "price_usd": 11.826477827607082,
                                            "symbol": "TRB",
                                            "name": "Tellor"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1873504.63,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6210,
                                            "price_usd": 0.360945325246123,
                                            "symbol": "SAND",
                                            "name": "The Sandbox"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 243220285.04,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 2157393.64,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7326,
                                            "price_usd": 2.2206543236327962,
                                            "symbol": "DEXE",
                                            "name": "DeXe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 5132138.53,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6669,
                                            "price_usd": 0.2955954734858841,
                                            "symbol": "CVP",
                                            "name": "PowerPool"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 21463.53,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 2581086.48,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13855,
                                            "price_usd": 8.344127675596797,
                                            "symbol": "ENS",
                                            "name": "Ethereum Name Service"
                                        }
                                    },
                                    {
                                        "wallet_address": "TNXoiAJ3dct8Fjg4M9fkLFh9S2v9TXc32G",
                                        "balance": 20620969.69,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3005675.19,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7672,
                                            "price_usd": 4.020318298953861,
                                            "symbol": "UNFI",
                                            "name": "Unifi Protocol DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 989860.07,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5964,
                                            "price_usd": 0.8790661478570492,
                                            "symbol": "TWT",
                                            "name": "Trust Wallet Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 4145557.58,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 489132678.39,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5007,
                                            "price_usd": 0.002362212928749703,
                                            "symbol": "TROY",
                                            "name": "TROY"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 211354.3,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1680,
                                            "price_usd": 4.293496800566868,
                                            "symbol": "ANT",
                                            "name": "Aragon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 573651.04,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11877,
                                            "price_usd": 1.1075951269820763,
                                            "symbol": "GAL",
                                            "name": "Galxe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 794980.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 12999,
                                            "price_usd": 16.11246853293979,
                                            "symbol": "SSV",
                                            "name": "ssv.network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 15523652.3,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3928,
                                            "price_usd": 0.04810576368371353,
                                            "symbol": "IDEX",
                                            "name": "IDEX"
                                        }
                                    },
                                    {
                                        "wallet_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
                                        "balance": 438719537.89,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 32818837.11,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3637,
                                            "price_usd": 0.09708981895527594,
                                            "symbol": "AERGO",
                                            "name": "Aergo"
                                        }
                                    },
                                    {
                                        "wallet_address": "D7JLeAgZK2TyFRFtjKwHMxhFjWvJ9gS5kj",
                                        "balance": 172192859,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 5500000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3964,
                                            "price_usd": 0.0020113234294809185,
                                            "symbol": "RSR",
                                            "name": "Reserve Rights"
                                        }
                                    },
                                    {
                                        "wallet_address": "MJwFHGandYUFJTTHHSXg3q6u7ge4af1n4N",
                                        "balance": 19999.8,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
                                        "balance": 2031492455585.57,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 16086,
                                            "price_usd": 4.4286497986976614e-07,
                                            "symbol": "BTT",
                                            "name": "BitTorrent(New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 7450000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 9175,
                                            "price_usd": 0.2612686901463243,
                                            "symbol": "MBOX",
                                            "name": "MOBOX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 50000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2505,
                                            "price_usd": 0.09280251123591385,
                                            "symbol": "BLZ",
                                            "name": "Bluzelle"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 292.36,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5864,
                                            "price_usd": 5781.231319319467,
                                            "symbol": "YFI",
                                            "name": "yearn.finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "DAYthKnkrWUHRENvtBwjemi6kFzk4K9SMr",
                                        "balance": 303275111,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 676637.4,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2570,
                                            "price_usd": 1.4634269063052316,
                                            "symbol": "TOMO",
                                            "name": "TomoChain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 873873137.37,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2398,
                                            "price_usd": 0.004864649064665026,
                                            "symbol": "KEY",
                                            "name": "SelfKey"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 1583.52,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 24760,
                                            "price_usd": 1822.4285403310957,
                                            "symbol": "WBETH",
                                            "name": "Wrapped Beacon ETH"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 21000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2320,
                                            "price_usd": 0.06009345770839763,
                                            "symbol": "UTK",
                                            "name": "Utrust"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 120279494.85,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2348,
                                            "price_usd": 0.04175809438375896,
                                            "symbol": "MDT",
                                            "name": "Measurable Data Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 22.54,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4023,
                                            "price_usd": 28655.28556241291,
                                            "symbol": "BTCB",
                                            "name": "Bitcoin BEP2"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 6899000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2010,
                                            "price_usd": 0.2767879319999242,
                                            "symbol": "ADA",
                                            "name": "Cardano"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 31927.92,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJCo98saj6WND61g1uuKwJ9GMWMT9WkJFo",
                                        "balance": 30000000,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 5488,
                                            "price_usd": 0.021092766705436302,
                                            "symbol": "JST",
                                            "name": "JUST"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 174349542.03,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 5488,
                                            "price_usd": 0.021092766705436302,
                                            "symbol": "JST",
                                            "name": "JUST"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 76000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11294,
                                            "price_usd": 0.06549878821976375,
                                            "symbol": "RARE",
                                            "name": "SuperRare"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 23104259,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3992,
                                            "price_usd": 0.044512810351528924,
                                            "symbol": "COTI",
                                            "name": "COTI"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 9950,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 706000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9119,
                                            "price_usd": 0.011255878881489326,
                                            "symbol": "TLM",
                                            "name": "Alien Worlds"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 511195.57,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7087,
                                            "price_usd": 1.421050310713961,
                                            "symbol": "DEGO",
                                            "name": "Dego Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 6498178.65,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2566,
                                            "price_usd": 0.17848954190804212,
                                            "symbol": "ONT",
                                            "name": "Ontology"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 1494.83,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 61000000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8707,
                                            "price_usd": 0.14197919934319755,
                                            "symbol": "ALPACA",
                                            "name": "Alpaca Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x29bdfbf7d27462a2d115748ace2bd71a2646946c",
                                        "balance": 16634.24,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 311903753.78,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2930,
                                            "price_usd": 0.00460138139420121,
                                            "symbol": "IQ",
                                            "name": "IQ"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 16096348.28,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5026,
                                            "price_usd": 0.0587380061789854,
                                            "symbol": "OXT",
                                            "name": "Orchid"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 413147678.8,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 20390383.93,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5117,
                                            "price_usd": 0.08502813254722748,
                                            "symbol": "OGN",
                                            "name": "Origin Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 700000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 19000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3798391.74,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8104,
                                            "price_usd": 0.26931518386189496,
                                            "symbol": "1INCH",
                                            "name": "1inch Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 2341021.27,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
                                        "balance": 22218826.63,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 10746,
                                            "price_usd": 0.07426541351824369,
                                            "symbol": "BSW",
                                            "name": "Biswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 93092.86,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8353,
                                            "price_usd": 1802.606053319381,
                                            "symbol": "BETH",
                                            "name": "Beacon ETH"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 56887991.74,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10603,
                                            "price_usd": 0.6406360524384285,
                                            "symbol": "IMX",
                                            "name": "Immutable"
                                        }
                                    },
                                    {
                                        "wallet_address": "TYASr5UV6HEcXatwdFQfmLVUqQQQMUxHLS",
                                        "balance": 32181520.43,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "TAzsQ9Gx8eqFNFSKbeXrbi45CuVPHzA8wr",
                                        "balance": 35775758.11,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 60125064.45,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11374,
                                            "price_usd": 0.09195658056835389,
                                            "symbol": "DAR",
                                            "name": "Mines of Dalarnia"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 89047.21,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 304461.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8613,
                                            "price_usd": 11.956718744103574,
                                            "symbol": "ALCX",
                                            "name": "Alchemix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 270437986.75,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6210,
                                            "price_usd": 0.360945325246123,
                                            "symbol": "SAND",
                                            "name": "The Sandbox"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 53063210.78,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 17145,
                                            "price_usd": 0.21967647440195656,
                                            "symbol": "LOKA",
                                            "name": "League of Kingdoms Arena"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 51103814.5,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4066,
                                            "price_usd": 0.06881139785105253,
                                            "symbol": "CHZ",
                                            "name": "Chiliz"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4800000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 10974,
                                            "price_usd": 0.13986644853762847,
                                            "symbol": "CHESS",
                                            "name": "Tranchess"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 19067376.16,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2505,
                                            "price_usd": 0.09280251123591385,
                                            "symbol": "BLZ",
                                            "name": "Bluzelle"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 23140841.29,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9148,
                                            "price_usd": 0.2417256834697115,
                                            "symbol": "DREP",
                                            "name": "Drep [new]"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9025,
                                            "price_usd": 0.2801214341472961,
                                            "symbol": "TRIBE",
                                            "name": "Tribe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 100651265.66,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6841,
                                            "price_usd": 0.08836830903452185,
                                            "symbol": "PHA",
                                            "name": "Phala Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 5194106097.76,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1886,
                                            "price_usd": 0.0007153914192280737,
                                            "symbol": "DENT",
                                            "name": "Dent"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 376481.59,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1732,
                                            "price_usd": 12.227137425133947,
                                            "symbol": "NMR",
                                            "name": "Numeraire"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 3030000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 15500000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8000,
                                            "price_usd": 1.730340030241288,
                                            "symbol": "LDO",
                                            "name": "Lido DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 82327691195.17,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6855,
                                            "price_usd": 6.490589252815927e-05,
                                            "symbol": "BIDR",
                                            "name": "BIDR"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3568402.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3773,
                                            "price_usd": 0.19884966503504237,
                                            "symbol": "FET",
                                            "name": "Fetch.ai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 600000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 526953.06,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8000,
                                            "price_usd": 1.730340030241288,
                                            "symbol": "LDO",
                                            "name": "Lido DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 2427370.78,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6758,
                                            "price_usd": 0.6827393888036559,
                                            "symbol": "SUSHI",
                                            "name": "SushiSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 17226.35,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x1fbe2acee135d991592f167ac371f3dd893a508b",
                                        "balance": 15507.6,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 20000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7455,
                                            "price_usd": 0.17083954103778173,
                                            "symbol": "AUDIO",
                                            "name": "Audius"
                                        }
                                    },
                                    {
                                        "wallet_address": "3Qxak1CZhLyZ7GVckKphLURdLBCjMfz9bA",
                                        "balance": 17669.23,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 17224907,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8290,
                                            "price_usd": 0.08842556946970717,
                                            "symbol": "SUPER",
                                            "name": "SuperVerse"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1863362.86,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 13663,
                                            "price_usd": 4.368098895101753,
                                            "symbol": "GNS",
                                            "name": "Gains Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 29178044.48,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2299,
                                            "price_usd": 0.30015180245867384,
                                            "symbol": "ELF",
                                            "name": "aelf"
                                        }
                                    },
                                    {
                                        "wallet_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
                                        "balance": 58837015.92,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 5488,
                                            "price_usd": 0.021092766705436302,
                                            "symbol": "JST",
                                            "name": "JUST"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 7114655.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6928,
                                            "price_usd": 0.6214878575632944,
                                            "symbol": "BEL",
                                            "name": "Bella Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 1002204604.98,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4066,
                                            "price_usd": 0.06881139785105253,
                                            "symbol": "CHZ",
                                            "name": "Chiliz"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 14000000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1886,
                                            "price_usd": 0.0007153914192280737,
                                            "symbol": "DENT",
                                            "name": "Dent"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe7804c37c13166ff0b37f5ae0bb07a3aebb6e245",
                                        "balance": 30500648.67,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1655742.35,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13502,
                                            "price_usd": 1.5184675678591322,
                                            "symbol": "WLD",
                                            "name": "Worldcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 1453427.19,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9040,
                                            "price_usd": 0.3526477419775614,
                                            "symbol": "PUNDIX",
                                            "name": "Pundi X (New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xBE0eB53F46cd790Cd13851d5EFf43D12404d33E8",
                                        "balance": 10010.05,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 90000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2416,
                                            "price_usd": 0.6840080701484711,
                                            "symbol": "THETA",
                                            "name": "Theta Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 7684916,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 11396,
                                            "price_usd": 0.2609301853967535,
                                            "symbol": "JOE",
                                            "name": "JOE"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 85036217.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3978,
                                            "price_usd": 0.10505888189769066,
                                            "symbol": "CHR",
                                            "name": "Chromia"
                                        }
                                    },
                                    {
                                        "wallet_address": "3LQUu4v9z6KNch71j7kbj8GPeAGUo1FW6a",
                                        "balance": 37926.98,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3580295.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11568,
                                            "price_usd": 0.5506115151550748,
                                            "symbol": "AGLD",
                                            "name": "Adventure Gold"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2117399468.98,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 20873,
                                            "price_usd": 0.0012846827263931979,
                                            "symbol": "LEVER",
                                            "name": "LeverFi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1500000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4134,
                                            "price_usd": 0.008795147806390458,
                                            "symbol": "AKRO",
                                            "name": "Akropolis"
                                        }
                                    },
                                    {
                                        "wallet_address": "3EbJfpmFgufYtzW9UFvf1GAfm2ted1Rwnr",
                                        "balance": 3821.08,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 2053640,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2011,
                                            "price_usd": 0.7340035324429687,
                                            "symbol": "XTZ",
                                            "name": "Tezos"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 4845384.53,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 27565,
                                            "price_usd": 0.38469232886433435,
                                            "symbol": "ARKM",
                                            "name": "Arkham"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 1000000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4943,
                                            "price_usd": 1.0000341428418609,
                                            "symbol": "DAI",
                                            "name": "Dai"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 61354.27,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 805265108,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5007,
                                            "price_usd": 0.002362212928749703,
                                            "symbol": "TROY",
                                            "name": "TROY"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 50000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2130,
                                            "price_usd": 0.26374312786015564,
                                            "symbol": "ENJ",
                                            "name": "Enjin Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJDENsfBJs4RFETt1X1W8wMDc8M5XnJhCe",
                                        "balance": 210995102.24,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "34HpHYiyQwg69gFmCq2BGHjF1DZnZnBeBP",
                                        "balance": 16306.63,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 380000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 14806,
                                            "price_usd": 0.010905799626187403,
                                            "symbol": "PEOPLE",
                                            "name": "ConstitutionDAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
                                        "balance": 8101419029.64,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 4206,
                                            "price_usd": 6.423059519400942e-05,
                                            "symbol": "WIN",
                                            "name": "WINkLink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 335.21,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2396,
                                            "price_usd": 1799.7166400864119,
                                            "symbol": "WETH",
                                            "name": "WETH"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 103500000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3330,
                                            "price_usd": 0.9984126185924139,
                                            "symbol": "USDP",
                                            "name": "Pax Dollar"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 30000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5690,
                                            "price_usd": 1.5999326532552023,
                                            "symbol": "RNDR",
                                            "name": "Render"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 73814161.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 50000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1697,
                                            "price_usd": 0.1874788142953606,
                                            "symbol": "BAT",
                                            "name": "Basic Attention Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 31793783.56,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6833,
                                            "price_usd": 0.6277856656093501,
                                            "symbol": "LIT",
                                            "name": "Litentry"
                                        }
                                    },
                                    {
                                        "wallet_address": "TNXoiAJ3dct8Fjg4M9fkLFh9S2v9TXc32G",
                                        "balance": 19122018.54,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 25900000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1853,
                                            "price_usd": 0.12927801778362752,
                                            "symbol": "OAX",
                                            "name": "OAX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1500000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2927,
                                            "price_usd": 0.9976887431042656,
                                            "symbol": "SUSD",
                                            "name": "sUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 601156989.68,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 199779,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1321,
                                            "price_usd": 16.32523143661133,
                                            "symbol": "ETC",
                                            "name": "Ethereum Classic"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 40000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4006,
                                            "price_usd": 0.04220216544088124,
                                            "symbol": "STPT",
                                            "name": "STP"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 5104414.76,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1808,
                                            "price_usd": 0.516594969575573,
                                            "symbol": "OMG",
                                            "name": "OMG Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 3567238.48,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 11396,
                                            "price_usd": 0.2609301853967535,
                                            "symbol": "JOE",
                                            "name": "JOE"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 2834315.75,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6953,
                                            "price_usd": 6.527456357216569,
                                            "symbol": "FXS",
                                            "name": "Frax Share"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 12000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7429,
                                            "price_usd": 0.8791895148928164,
                                            "symbol": "LQTY",
                                            "name": "Liquity"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xeae7380dd4cef6fbd1144f49e4d1e6964258a4f4",
                                        "balance": 671366,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 11797986.55,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3637,
                                            "price_usd": 0.09708981895527594,
                                            "symbol": "AERGO",
                                            "name": "Aergo"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 86958155.93,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2130,
                                            "price_usd": 0.26374312786015564,
                                            "symbol": "ENJ",
                                            "name": "Enjin Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 299311.87,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11156,
                                            "price_usd": 2.0188445185052615,
                                            "symbol": "DYDX",
                                            "name": "dYdX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 6000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2570,
                                            "price_usd": 1.4634269063052316,
                                            "symbol": "TOMO",
                                            "name": "TomoChain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 10485455.41,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7412,
                                            "price_usd": 0.23065466154410075,
                                            "symbol": "UFT",
                                            "name": "UniLend"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 158899.95,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3391519.91,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1697,
                                            "price_usd": 0.1874788142953606,
                                            "symbol": "BAT",
                                            "name": "Basic Attention Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 1883147108116.13,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 24478,
                                            "price_usd": 1.2043396244619398e-06,
                                            "symbol": "PEPE",
                                            "name": "Pepe"
                                        }
                                    },
                                    {
                                        "wallet_address": "DJfU2p6woQ9GiBdiXsWZWJnJ9uDdZfSSNC",
                                        "balance": 548133458.84,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 9536662.16,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3714,
                                            "price_usd": 0.05945232953471845,
                                            "symbol": "LTO",
                                            "name": "LTO Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 970000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4066,
                                            "price_usd": 0.06881139785105253,
                                            "symbol": "CHZ",
                                            "name": "Chiliz"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 1200000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1757,
                                            "price_usd": 0.005033779682647976,
                                            "symbol": "FUN",
                                            "name": "FUNToken"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 43182201.21,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4092,
                                            "price_usd": 0.11765989588608315,
                                            "symbol": "DUSK",
                                            "name": "Dusk"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 6000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h",
                                        "balance": 52006.97,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "DFyohYD3bMXCEg1TdMfdy1J7dYfK4shhPf",
                                        "balance": 53632466.99,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 29438145.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11307,
                                            "price_usd": 0.07810790578253467,
                                            "symbol": "BETA",
                                            "name": "Beta Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
                                        "balance": 6920743.25,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 102319654,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 21846,
                                            "price_usd": 0.21727459369047844,
                                            "symbol": "ID",
                                            "name": "SPACE ID"
                                        }
                                    },
                                    {
                                        "wallet_address": "38DN2uFMZPiHLHJigfv4kWC9JWJrNnhLcn",
                                        "balance": 40041.05,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 128900000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1817,
                                            "price_usd": 0.1412101306862558,
                                            "symbol": "VGX",
                                            "name": "Voyager Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 391274.68,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3640,
                                            "price_usd": 7.005585781859719,
                                            "symbol": "LPT",
                                            "name": "Livepeer"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 7078562.37,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5444,
                                            "price_usd": 0.13736289216940076,
                                            "symbol": "CTSI",
                                            "name": "Cartesi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 199310.36,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6859,
                                            "price_usd": 22.77213558860157,
                                            "symbol": "FARM",
                                            "name": "Harvest Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 148255,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7672,
                                            "price_usd": 4.020318298953861,
                                            "symbol": "UNFI",
                                            "name": "Unifi Protocol DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 27000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1896,
                                            "price_usd": 0.19387387587753957,
                                            "symbol": "ZRX",
                                            "name": "0x Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 116083.84,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13855,
                                            "price_usd": 8.344127675596797,
                                            "symbol": "ENS",
                                            "name": "Ethereum Name Service"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 163290.35,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 14335672.27,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6928,
                                            "price_usd": 0.6214878575632944,
                                            "symbol": "BEL",
                                            "name": "Bella Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 919.91,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 7185529399.02,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 5762429,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 12147,
                                            "price_usd": 0.5266919329889396,
                                            "symbol": "SYN",
                                            "name": "Synapse"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xF977814e90dA44bFA03b6295A0616a897441aceC",
                                        "balance": 12796130.16,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 13502,
                                            "price_usd": 1.5184675678591322,
                                            "symbol": "WLD",
                                            "name": "Worldcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJCo98saj6WND61g1uuKwJ9GMWMT9WkJFo",
                                        "balance": 150034239437.38,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 4206,
                                            "price_usd": 6.423059519400942e-05,
                                            "symbol": "WIN",
                                            "name": "WINkLink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 100000000.01,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3773,
                                            "price_usd": 0.19884966503504237,
                                            "symbol": "FET",
                                            "name": "Fetch.ai"
                                        }
                                    },
                                    {
                                        "wallet_address": "MB8nnFMvR5cgvpzQ1QXTDVfUM91BcsLH3k",
                                        "balance": 513259.29,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 11710661,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7224,
                                            "price_usd": 0.10730965957273395,
                                            "symbol": "DODO",
                                            "name": "DODO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 30000015.62,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 10683856.7,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11877,
                                            "price_usd": 1.1075951269820763,
                                            "symbol": "GAL",
                                            "name": "Galxe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 45260186.66,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1934,
                                            "price_usd": 0.20263980290989594,
                                            "symbol": "LRC",
                                            "name": "Loopring"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 23493693.37,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 11374,
                                            "price_usd": 0.09195658056835389,
                                            "symbol": "DAR",
                                            "name": "Mines of Dalarnia"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 2424294.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1966,
                                            "price_usd": 0.33374694855015846,
                                            "symbol": "MANA",
                                            "name": "Decentraland"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 140795340.56,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4705670.62,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5794,
                                            "price_usd": 0.11160503640959443,
                                            "symbol": "PNT",
                                            "name": "pNetwork"
                                        }
                                    },
                                    {
                                        "wallet_address": "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo",
                                        "balance": 248597.39,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xeb2d2f1b8c558a40207669291fda468e50c8a0bb",
                                        "balance": 8590.2,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 13603688.26,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2058,
                                            "price_usd": 0.09245317298578626,
                                            "symbol": "AST",
                                            "name": "AirSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "TV6MuMXfmLbBqPZvBHdwFsDnQeVfnmiuSi",
                                        "balance": 65095231.16,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 139030166.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3928,
                                            "price_usd": 0.04810576368371353,
                                            "symbol": "IDEX",
                                            "name": "IDEX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 49180960,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 14783,
                                            "price_usd": 0.6777151316478582,
                                            "symbol": "MAGIC",
                                            "name": "MAGIC"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 334989493.01,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6958,
                                            "price_usd": 0.0156639410640151,
                                            "symbol": "ACH",
                                            "name": "Alchemy Pay"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 70000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5805,
                                            "price_usd": 11.449580596258247,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3148345.17,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7226,
                                            "price_usd": 7.206011020391402,
                                            "symbol": "INJ",
                                            "name": "Injective"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 32900000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3911,
                                            "price_usd": 0.319212189140852,
                                            "symbol": "OCEAN",
                                            "name": "Ocean Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 1539463587.89,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 9288,
                                            "price_usd": 0.005741810263315303,
                                            "symbol": "QI",
                                            "name": "BENQI"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJDENsfBJs4RFETt1X1W8wMDc8M5XnJhCe",
                                        "balance": 36991001.5,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 34875828.55,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5444,
                                            "price_usd": 0.13736289216940076,
                                            "symbol": "CTSI",
                                            "name": "Cartesi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 87374483.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4134,
                                            "price_usd": 0.008795147806390458,
                                            "symbol": "AKRO",
                                            "name": "Akropolis"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 479881.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8000,
                                            "price_usd": 1.730340030241288,
                                            "symbol": "LDO",
                                            "name": "Lido DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "MQd1fJwqBJvwLuyhr17PhEFx1swiqDbPQS",
                                        "balance": 2003282.13,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 293157755.25,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 4400000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9308,
                                            "price_usd": 3.2036894083443537,
                                            "symbol": "PYR",
                                            "name": "Vulcan Forged PYR"
                                        }
                                    },
                                    {
                                        "wallet_address": "M8T1B2Z97gVdvmfkQcAtYbEepune1tzGua",
                                        "balance": 2504667.35,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 5108854.03,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9040,
                                            "price_usd": 0.3526477419775614,
                                            "symbol": "PUNDIX",
                                            "name": "Pundi X (New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 200000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 30000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3992,
                                            "price_usd": 0.044512810351528924,
                                            "symbol": "COTI",
                                            "name": "COTI"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 587786281.17,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3783,
                                            "price_usd": 0.021526053031444267,
                                            "symbol": "ANKR",
                                            "name": "Ankr"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9f8c163cba728e99993abe7495f06c0a3c8ac8b9",
                                        "balance": 48833206.11,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 70107556,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 21846,
                                            "price_usd": 0.21727459369047844,
                                            "symbol": "ID",
                                            "name": "SPACE ID"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 2000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7859,
                                            "price_usd": 2.3115699996508043,
                                            "symbol": "BADGER",
                                            "name": "Badger DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "DPAMdZsSirVBGeDR9sE1LJXkwG6AQSNAMW",
                                        "balance": 358324741,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 4707507.85,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "DEvUEF9VrXbKf5rdaQCUzeh4MvZxd3Zx5T",
                                        "balance": 97166076,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 110200384.07,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4039,
                                            "price_usd": 0.04687375470683488,
                                            "symbol": "ARPA",
                                            "name": "ARPA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 40875960.89,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1772,
                                            "price_usd": 0.2534620883650551,
                                            "symbol": "STORJ",
                                            "name": "Storj"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 36459.14,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5692,
                                            "price_usd": 47.02453637096567,
                                            "symbol": "COMP",
                                            "name": "Compound"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x161ba15a5f335c9f06bb5bbb0a9ce14076fbb645",
                                        "balance": 16586.53,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 3144715,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "D73RQLGWW9TBT2AKspEP24wLiXFrXvnTqX",
                                        "balance": 67455316,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 10451040.39,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10688,
                                            "price_usd": 0.2624587816246438,
                                            "symbol": "YGG",
                                            "name": "Yield Guild Games"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 10000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6138,
                                            "price_usd": 0.23526694555057048,
                                            "symbol": "DIA",
                                            "name": "DIA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 264639611.38,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 1000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4195,
                                            "price_usd": 1.0268221155987947,
                                            "symbol": "FTT",
                                            "name": "FTX Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "DCxFJEWsYJFnC3HP7YfZdsd3X43ttQA79Z",
                                        "balance": 205763823,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 312607023,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5007,
                                            "price_usd": 0.002362212928749703,
                                            "symbol": "TROY",
                                            "name": "TROY"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 18080016.65,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2776,
                                            "price_usd": 0.5486064630311943,
                                            "symbol": "AVA",
                                            "name": "Travala.com"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 29181622,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2019,
                                            "price_usd": 0.04386865599482222,
                                            "symbol": "VIB",
                                            "name": "Viberate"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 930000000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5824,
                                            "price_usd": 0.0015259345050299268,
                                            "symbol": "SLP",
                                            "name": "Smooth Love Potion"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe2fc31f816a9b94326492132018c3aecc4a93ae1",
                                        "balance": 3884.54,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 17185720.59,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 30738.85,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 24760,
                                            "price_usd": 1822.4285403310957,
                                            "symbol": "WBETH",
                                            "name": "Wrapped Beacon ETH"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 222415540968.1,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 4206,
                                            "price_usd": 6.423059519400942e-05,
                                            "symbol": "WIN",
                                            "name": "WINkLink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1277380.26,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 12147,
                                            "price_usd": 0.5266919329889396,
                                            "symbol": "SYN",
                                            "name": "Synapse"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 10456642.15,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1934,
                                            "price_usd": 0.20263980290989594,
                                            "symbol": "LRC",
                                            "name": "Loopring"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 6072972.44,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2694,
                                            "price_usd": 0.6298398293491478,
                                            "symbol": "NEXO",
                                            "name": "Nexo"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 7312356.82,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8104,
                                            "price_usd": 0.26931518386189496,
                                            "symbol": "1INCH",
                                            "name": "1inch Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 444455997.5,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 10529,
                                            "price_usd": 0.005463450933392547,
                                            "symbol": "SUN",
                                            "name": "Sun (New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 15302991.08,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 4790705304.61,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7080,
                                            "price_usd": 0.02084554777171437,
                                            "symbol": "GALA",
                                            "name": "Gala"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x01c952174c24e1210d26961d456a77a39e1f0bb0",
                                        "balance": 15592.09,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 150874085.15,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10903,
                                            "price_usd": 0.15167140199133478,
                                            "symbol": "C98",
                                            "name": "Coin98"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 220000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2424,
                                            "price_usd": 0.1968938943092629,
                                            "symbol": "AGIX",
                                            "name": "SingularityNET"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 23620687,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2299,
                                            "price_usd": 0.30015180245867384,
                                            "symbol": "ELF",
                                            "name": "aelf"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 26579752.01,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 18934,
                                            "price_usd": 0.5927043786609867,
                                            "symbol": "STG",
                                            "name": "Stargate Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 3164668901925.01,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 16086,
                                            "price_usd": 4.4286497986976614e-07,
                                            "symbol": "BTT",
                                            "name": "BitTorrent(New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 353981.92,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6843,
                                            "price_usd": 1.4732732627569565,
                                            "symbol": "RAD",
                                            "name": "Radworks"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 166811.1,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8536,
                                            "price_usd": 3.06261767866833,
                                            "symbol": "MASK",
                                            "name": "Mask Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 26000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 13502,
                                            "price_usd": 1.5184675678591322,
                                            "symbol": "WLD",
                                            "name": "Worldcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x515b72ed8a97f42c568d6a143232775018f133c8",
                                        "balance": 13781.11,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 45797.88,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8613,
                                            "price_usd": 11.956718744103574,
                                            "symbol": "ALCX",
                                            "name": "Alchemix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 322566.25,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6953,
                                            "price_usd": 6.527456357216569,
                                            "symbol": "FXS",
                                            "name": "Frax Share"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 6000000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 7255,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 30993992.19,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2348,
                                            "price_usd": 0.04175809438375896,
                                            "symbol": "MDT",
                                            "name": "Measurable Data Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 5832.83,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4705,
                                            "price_usd": 1894.3189653673944,
                                            "symbol": "PAXG",
                                            "name": "PAX Gold"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 239416830.74,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4118,
                                            "price_usd": 0.018444818081190584,
                                            "symbol": "FOR",
                                            "name": "ForTube"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 28200000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2130,
                                            "price_usd": 0.26374312786015564,
                                            "symbol": "ENJ",
                                            "name": "Enjin Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1996795.28,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4943,
                                            "price_usd": 1.0000341428418609,
                                            "symbol": "DAI",
                                            "name": "Dai"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 839723.85,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7226,
                                            "price_usd": 7.206011020391402,
                                            "symbol": "INJ",
                                            "name": "Injective"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 26849820.25,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7725,
                                            "price_usd": 0.03422768065547463,
                                            "symbol": "TRU",
                                            "name": "TrueFi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 630000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8425,
                                            "price_usd": 0.003640793400236315,
                                            "symbol": "JASMY",
                                            "name": "JasmyCoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 10000001,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1853,
                                            "price_usd": 0.12927801778362752,
                                            "symbol": "OAX",
                                            "name": "OAX"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 102828.8,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 606192.54,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1788,
                                            "price_usd": 1.1649219812892724,
                                            "symbol": "MTL",
                                            "name": "Metal DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 23050000000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 14371,
                                            "price_usd": 3.7885780448925484e-05,
                                            "symbol": "IHC",
                                            "name": "Inflation Hedging Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 64149157.48,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18069,
                                            "price_usd": 0.18076752837525792,
                                            "symbol": "GMT",
                                            "name": "STEPN"
                                        }
                                    },
                                    {
                                        "wallet_address": "TYASr5UV6HEcXatwdFQfmLVUqQQQMUxHLS",
                                        "balance": 173285876.03,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4976a4a02f38326660d17bf34b431dc6e2eb2327",
                                        "balance": 21370.33,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "TQrY8tryqsYVCYS3MFbtffiPp2ccyn4STm",
                                        "balance": 21543983.59,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 1958,
                                            "price_usd": 0.07458628890858825,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 598502.9,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7083,
                                            "price_usd": 5.461323768679141,
                                            "symbol": "UNI",
                                            "name": "Uniswap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xe7804c37c13166ff0b37f5ae0bb07a3aebb6e245",
                                        "balance": 10993993.88,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 6400000.4,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4092,
                                            "price_usd": 0.11765989588608315,
                                            "symbol": "DUSK",
                                            "name": "Dusk"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 32966798541026.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5994,
                                            "price_usd": 9.265611730463855e-06,
                                            "symbol": "SHIB",
                                            "name": "Shiba Inu"
                                        }
                                    },
                                    {
                                        "wallet_address": "TAzsQ9Gx8eqFNFSKbeXrbi45CuVPHzA8wr",
                                        "balance": 121235896.69,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xa180fe01b906a1be37be6c534a3300785b20d947",
                                        "balance": 14698.84,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 900000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3814,
                                            "price_usd": 0.012595021044361457,
                                            "symbol": "CELR",
                                            "name": "Celer Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3096020178.4,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 16434,
                                            "price_usd": 0.0024696020308150666,
                                            "symbol": "OOKI",
                                            "name": "Ooki Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 3897186.4,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3773,
                                            "price_usd": 0.19884966503504237,
                                            "symbol": "FET",
                                            "name": "Fetch.ai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 16218710.99,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11877,
                                            "price_usd": 1.1075951269820763,
                                            "symbol": "GAL",
                                            "name": "Galxe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 28000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 22710,
                                            "price_usd": 0.01973121187905417,
                                            "symbol": "VIDT",
                                            "name": "VIDT DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 500930895.17,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3890,
                                            "price_usd": 0.6212883601060246,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 13164349.59,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8536,
                                            "price_usd": 3.06261767866833,
                                            "symbol": "MASK",
                                            "name": "Mask Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 2231445.89,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2586,
                                            "price_usd": 2.321664881332331,
                                            "symbol": "SNX",
                                            "name": "Synthetix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 23754661.65,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8000,
                                            "price_usd": 1.730340030241288,
                                            "symbol": "LDO",
                                            "name": "Lido DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 485454.79,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6783,
                                            "price_usd": 5.351594584639869,
                                            "symbol": "AXS",
                                            "name": "Axie Infinity"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1fnd0k5l4p3ck2j9x9dp36chk059w977pszdgdz",
                                        "balance": 189501856.88,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3945,
                                            "price_usd": 0.010567727184514344,
                                            "symbol": "ONE",
                                            "name": "Harmony"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xF977814e90dA44bFA03b6295A0616a897441aceC",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 11840,
                                            "price_usd": 1.4558134437345407,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1637,
                                            "price_usd": 1.1341860890318043,
                                            "symbol": "RLC",
                                            "name": "iExec RLC"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 25082750.22,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3029,
                                            "price_usd": 0.36414956983259683,
                                            "symbol": "FLUX",
                                            "name": "Flux"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x8894e0a0c962cb723c1976a4421c95949be2d4e3",
                                        "balance": 1289261.45,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7186,
                                            "price_usd": 1.4207588530522008,
                                            "symbol": "CAKE",
                                            "name": "PancakeSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 454183.21,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2586,
                                            "price_usd": 2.321664881332331,
                                            "symbol": "SNX",
                                            "name": "Synthetix"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 10000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5444,
                                            "price_usd": 0.13736289216940076,
                                            "symbol": "CTSI",
                                            "name": "Cartesi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 108920021,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18037,
                                            "price_usd": 0.23378068221563175,
                                            "symbol": "MAV",
                                            "name": "Maverick Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9f8c163cba728e99993abe7495f06c0a3c8ac8b9",
                                        "balance": 943929.37,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 18934,
                                            "price_usd": 0.5927043786609867,
                                            "symbol": "STG",
                                            "name": "Stargate Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1195873153.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1757,
                                            "price_usd": 0.005033779682647976,
                                            "symbol": "FUN",
                                            "name": "FUNToken"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 45227444.86,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7186,
                                            "price_usd": 1.4207588530522008,
                                            "symbol": "CAKE",
                                            "name": "PancakeSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 11197022.13,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6538,
                                            "price_usd": 0.5468384145822828,
                                            "symbol": "CRV",
                                            "name": "Curve DAO Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 90535.04,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6953,
                                            "price_usd": 6.527456357216569,
                                            "symbol": "FXS",
                                            "name": "Frax Share"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 64620012.54,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2071,
                                            "price_usd": 0.07214579105943983,
                                            "symbol": "REQ",
                                            "name": "Request"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 377046.95,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11156,
                                            "price_usd": 2.0188445185052615,
                                            "symbol": "DYDX",
                                            "name": "dYdX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 196652688.83,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10188,
                                            "price_usd": 0.07619598469410216,
                                            "symbol": "ATA",
                                            "name": "Automata Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 13876545.18,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2570,
                                            "price_usd": 1.4634269063052316,
                                            "symbol": "TOMO",
                                            "name": "TomoChain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 50179454.57,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2143,
                                            "price_usd": 0.022284337066153518,
                                            "symbol": "DATA",
                                            "name": "Streamr"
                                        }
                                    },
                                    {
                                        "wallet_address": "3FHNBLobJnbCTFTVakh5TXmEneyf5PT61B",
                                        "balance": 31275.35,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "MLkNzCps6cXou2DELVfxDuRC4uZGwr397o",
                                        "balance": 200940,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 139998.49,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 11625737.03,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9931,
                                            "price_usd": 0.05136655573695775,
                                            "symbol": "SNM",
                                            "name": "SONM (BEP-20)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1139235.23,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6783,
                                            "price_usd": 5.351594584639869,
                                            "symbol": "AXS",
                                            "name": "Axie Infinity"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 36033766,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5964,
                                            "price_usd": 0.8790661478570492,
                                            "symbol": "TWT",
                                            "name": "Trust Wallet Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 350000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4066,
                                            "price_usd": 0.06881139785105253,
                                            "symbol": "CHZ",
                                            "name": "Chiliz"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 234000000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 23635,
                                            "price_usd": 0.21952213820595448,
                                            "symbol": "BNX",
                                            "name": "BinaryX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1239493129.67,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6958,
                                            "price_usd": 0.0156639410640151,
                                            "symbol": "ACH",
                                            "name": "Alchemy Pay"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xacd03d601e5bb1b275bb94076ff46ed9d753435a",
                                        "balance": 1702282.01,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 24781,
                                            "price_usd": 4.028895414964144,
                                            "symbol": "CYBER",
                                            "name": "CyberConnect"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 188285.98,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7440,
                                            "price_usd": 2.7820703816745738,
                                            "symbol": "BOND",
                                            "name": "BarnBridge"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 919411910.49,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4066,
                                            "price_usd": 0.06881139785105253,
                                            "symbol": "CHZ",
                                            "name": "Chiliz"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 8650000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6950,
                                            "price_usd": 0.47690763728000146,
                                            "symbol": "PERP",
                                            "name": "Perpetual Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4817300,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5444,
                                            "price_usd": 0.13736289216940076,
                                            "symbol": "CTSI",
                                            "name": "Cartesi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 32597755.98,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 280823.18,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1680,
                                            "price_usd": 4.293496800566868,
                                            "symbol": "ANT",
                                            "name": "Aragon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 605457.4,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5690,
                                            "price_usd": 1.5999326532552023,
                                            "symbol": "RNDR",
                                            "name": "Render"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 70000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2424,
                                            "price_usd": 0.1968938943092629,
                                            "symbol": "AGIX",
                                            "name": "SingularityNET"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 354991295.06,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1759,
                                            "price_usd": 0.022819467904048246,
                                            "symbol": "SNT",
                                            "name": "Status"
                                        }
                                    },
                                    {
                                        "wallet_address": "3LcgLHzTvjLKBixBvkKGiadtiw2GBSKKqH",
                                        "balance": 1999.8,
                                        "platform": {
                                            "crypto_id": 1,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        },
                                        "currency": {
                                            "crypto_id": 1,
                                            "price_usd": 28651.886436232886,
                                            "symbol": "BTC",
                                            "name": "Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 20000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2132,
                                            "price_usd": 0.142382210141333,
                                            "symbol": "POWR",
                                            "name": "Powerledger"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xacd03d601e5bb1b275bb94076ff46ed9d753435a",
                                        "balance": 75986538.27,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 27092291.54,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5882,
                                            "price_usd": 0.2632025470029881,
                                            "symbol": "FIS",
                                            "name": "StaFi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 11519982.1,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 22461,
                                            "price_usd": 0.34575179462685857,
                                            "symbol": "HFT",
                                            "name": "Hashflow"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 107327879.56,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2010,
                                            "price_usd": 0.2767879319999242,
                                            "symbol": "ADA",
                                            "name": "Cardano"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 2028.23,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 24760,
                                            "price_usd": 1822.4285403310957,
                                            "symbol": "WBETH",
                                            "name": "Wrapped Beacon ETH"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 104270408.27,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1934,
                                            "price_usd": 0.20263980290989594,
                                            "symbol": "LRC",
                                            "name": "Loopring"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 3708864.42,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18876,
                                            "price_usd": 1.7887230786187478,
                                            "symbol": "APE",
                                            "name": "ApeCoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 67932178.77,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 11374,
                                            "price_usd": 0.09195658056835389,
                                            "symbol": "DAR",
                                            "name": "Mines of Dalarnia"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 10406407.25,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 17070577.68,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8766,
                                            "price_usd": 0.8523112173510031,
                                            "symbol": "ALICE",
                                            "name": "MyNeighborAlice"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 58027411.11,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 6210,
                                            "price_usd": 0.360945325246123,
                                            "symbol": "SAND",
                                            "name": "The Sandbox"
                                        }
                                    },
                                    {
                                        "wallet_address": "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9",
                                        "balance": 10000000163,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 4206,
                                            "price_usd": 6.423059519400942e-05,
                                            "symbol": "WIN",
                                            "name": "WINkLink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 50000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2780,
                                            "price_usd": 0.09735616019240688,
                                            "symbol": "NKN",
                                            "name": "NKN"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 3477,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 7543798.67,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 195594587.16,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3783,
                                            "price_usd": 0.021526053031444267,
                                            "symbol": "ANKR",
                                            "name": "Ankr"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 18241111.82,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 86657197,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 27565,
                                            "price_usd": 0.38469232886433435,
                                            "symbol": "ARKM",
                                            "name": "Arkham"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 571119.07,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 85803284.55,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2320,
                                            "price_usd": 0.06009345770839763,
                                            "symbol": "UTK",
                                            "name": "Utrust"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 214374266.03,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3783,
                                            "price_usd": 0.021526053031444267,
                                            "symbol": "ANKR",
                                            "name": "Ankr"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 219588.32,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7859,
                                            "price_usd": 2.3115699996508043,
                                            "symbol": "BADGER",
                                            "name": "Badger DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 677271,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5617,
                                            "price_usd": 1.4942992899842977,
                                            "symbol": "UMA",
                                            "name": "UMA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 105094246,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 21106,
                                            "price_usd": 0.2737185776938926,
                                            "symbol": "RDNT",
                                            "name": "Radiant Capital"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 7878483,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 52,
                                            "price_usd": 0.5878633783129905,
                                            "symbol": "XRP",
                                            "name": "XRP"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 101208813.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2780,
                                            "price_usd": 0.09735616019240688,
                                            "symbol": "NKN",
                                            "name": "NKN"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 25460569,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3513,
                                            "price_usd": 0.21750825430440904,
                                            "symbol": "FTM",
                                            "name": "Fantom"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb142q467df6jun6rt5u2ar58sp47hm5f9wvz2cvg",
                                        "balance": 15715698.77,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4039,
                                            "price_usd": 0.04687375470683488,
                                            "symbol": "ARPA",
                                            "name": "ARPA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 36511023.13,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1759,
                                            "price_usd": 0.022819467904048246,
                                            "symbol": "SNT",
                                            "name": "Status"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 5426480.35,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3330,
                                            "price_usd": 0.9984126185924139,
                                            "symbol": "USDP",
                                            "name": "Pax Dollar"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1459144.04,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 23037,
                                            "price_usd": 0.3614706657835475,
                                            "symbol": "HIFI",
                                            "name": "Hifi Finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 26589870.43,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5794,
                                            "price_usd": 0.11160503640959443,
                                            "symbol": "PNT",
                                            "name": "pNetwork"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 28000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1831,
                                            "price_usd": 210.29189810012312,
                                            "symbol": "BCH",
                                            "name": "Bitcoin Cash"
                                        }
                                    },
                                    {
                                        "wallet_address": "TWd4WrZ9wn84f5x1hZhL4DHvk738ns5jwb",
                                        "balance": 6181293.04,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "MBjKmoDwkuUbtnVd4vjymxjJx7Crca2s1z",
                                        "balance": 87208.48,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJCo98saj6WND61g1uuKwJ9GMWMT9WkJFo",
                                        "balance": 12000000000000,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 16086,
                                            "price_usd": 4.4286497986976614e-07,
                                            "symbol": "BTT",
                                            "name": "BitTorrent(New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 1839662318304.76,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5994,
                                            "price_usd": 9.265611730463855e-06,
                                            "symbol": "SHIB",
                                            "name": "Shiba Inu"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 11977116.01,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 15161894.77,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3992,
                                            "price_usd": 0.044512810351528924,
                                            "symbol": "COTI",
                                            "name": "COTI"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 11979177735.01,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11289,
                                            "price_usd": 0.0004193090800843014,
                                            "symbol": "SPELL",
                                            "name": "Spell Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xacd03d601e5bb1b275bb94076ff46ed9d753435a",
                                        "balance": 784779.84,
                                        "platform": {
                                            "crypto_id": 11840,
                                            "symbol": "OP",
                                            "name": "Optimism"
                                        },
                                        "currency": {
                                            "crypto_id": 13502,
                                            "price_usd": 1.5184675678591322,
                                            "symbol": "WLD",
                                            "name": "Worldcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 218125940.42,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4039,
                                            "price_usd": 0.04687375470683488,
                                            "symbol": "ARPA",
                                            "name": "ARPA"
                                        }
                                    },
                                    {
                                        "wallet_address": "D7QZnXec5bkMyokPFPh6v4WAw5VF5TocAy",
                                        "balance": 32596585.98,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 6451.15,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1518,
                                            "price_usd": 1143.5404761450968,
                                            "symbol": "MKR",
                                            "name": "Maker"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 394532.64,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5617,
                                            "price_usd": 1.4942992899842977,
                                            "symbol": "UMA",
                                            "name": "UMA"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 52000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1966,
                                            "price_usd": 0.33374694855015846,
                                            "symbol": "MANA",
                                            "name": "Decentraland"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 78464921.06,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3928,
                                            "price_usd": 0.04810576368371353,
                                            "symbol": "IDEX",
                                            "name": "IDEX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 270000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3992,
                                            "price_usd": 0.044512810351528924,
                                            "symbol": "COTI",
                                            "name": "COTI"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 30000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2058,
                                            "price_usd": 0.09245317298578626,
                                            "symbol": "AST",
                                            "name": "AirSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 2100000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 825,
                                            "price_usd": 0.9987244301917502,
                                            "symbol": "USDT",
                                            "name": "Tether USDt"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 4277440.71,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 18037,
                                            "price_usd": 0.23378068221563175,
                                            "symbol": "MAV",
                                            "name": "Maverick Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 16293178.94,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 1926217.41,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4120,
                                            "price_usd": 3.9668892439470778,
                                            "symbol": "PROM",
                                            "name": "Prom"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 4170768.58,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1680,
                                            "price_usd": 4.293496800566868,
                                            "symbol": "ANT",
                                            "name": "Aragon"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 161163891,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 3408,
                                            "price_usd": 1.000036334148408,
                                            "symbol": "USDC",
                                            "name": "USD Coin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 17583466.93,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 21846,
                                            "price_usd": 0.21727459369047844,
                                            "symbol": "ID",
                                            "name": "SPACE ID"
                                        }
                                    },
                                    {
                                        "wallet_address": "TJCo98saj6WND61g1uuKwJ9GMWMT9WkJFo",
                                        "balance": 646367699.08,
                                        "platform": {
                                            "crypto_id": 1958,
                                            "symbol": "TRX",
                                            "name": "TRON"
                                        },
                                        "currency": {
                                            "crypto_id": 2563,
                                            "price_usd": 0.9992077114517395,
                                            "symbol": "TUSD",
                                            "name": "TrueUSD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 363.93,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5864,
                                            "price_usd": 5781.231319319467,
                                            "symbol": "YFI",
                                            "name": "yearn.finance"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 3254536.4,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 17050,
                                            "price_usd": 1.5127384084033175,
                                            "symbol": "MULTI",
                                            "name": "Multichain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 501417.5,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 11841,
                                            "price_usd": 1.0593171826187295,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 47171206.07,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7501,
                                            "price_usd": 0.1725972177179486,
                                            "symbol": "WOO",
                                            "name": "WOO Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x21a31ee1afc51d94c2efccaa2092ad1028285549",
                                        "balance": 432.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3717,
                                            "price_usd": 28617.101745242293,
                                            "symbol": "WBTC",
                                            "name": "Wrapped Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 33577514,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3911,
                                            "price_usd": 0.319212189140852,
                                            "symbol": "OCEAN",
                                            "name": "Ocean Protocol"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 64013751.19,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10188,
                                            "price_usd": 0.07619598469410216,
                                            "symbol": "ATA",
                                            "name": "Automata Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x56eddb7aa87536c09ccc2793473599fd21a8b17f",
                                        "balance": 27376.18,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x9696f59e4d72e237be84ffd425dcad154bf96976",
                                        "balance": 18103.11,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1027,
                                            "price_usd": 1800.5320387732727,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 15388.81,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8719,
                                            "price_usd": 49.182340809909334,
                                            "symbol": "ILV",
                                            "name": "Illuvium"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 9938850.54,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 10903,
                                            "price_usd": 0.15167140199133478,
                                            "symbol": "C98",
                                            "name": "Coin98"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 34161975.85,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4092,
                                            "price_usd": 0.11765989588608315,
                                            "symbol": "DUSK",
                                            "name": "Dusk"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 648272.47,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3794,
                                            "price_usd": 7.854000248929436,
                                            "symbol": "ATOM",
                                            "name": "Cosmos"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 20995007.13,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9040,
                                            "price_usd": 0.3526477419775614,
                                            "symbol": "PUNDIX",
                                            "name": "Pundi X (New)"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2592931900,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6951,
                                            "price_usd": 0.001406638987787203,
                                            "symbol": "REEF",
                                            "name": "Reef"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 4056495,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3773,
                                            "price_usd": 0.19884966503504237,
                                            "symbol": "FET",
                                            "name": "Fetch.ai"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 58400000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7501,
                                            "price_usd": 0.1725972177179486,
                                            "symbol": "WOO",
                                            "name": "WOO Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 303.34,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3717,
                                            "price_usd": 28617.101745242293,
                                            "symbol": "WBTC",
                                            "name": "Wrapped Bitcoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 11963.86,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1831,
                                            "price_usd": 210.29189810012312,
                                            "symbol": "BCH",
                                            "name": "Bitcoin Cash"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 2323892.52,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 11156,
                                            "price_usd": 2.0188445185052615,
                                            "symbol": "DYDX",
                                            "name": "dYdX"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2502498.18,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 9025,
                                            "price_usd": 0.2801214341472961,
                                            "symbol": "TRIBE",
                                            "name": "Tribe"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 7000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5794,
                                            "price_usd": 0.11160503640959443,
                                            "symbol": "PNT",
                                            "name": "pNetwork"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 15099.39,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7278,
                                            "price_usd": 60.34191176295828,
                                            "symbol": "AAVE",
                                            "name": "Aave"
                                        }
                                    },
                                    {
                                        "wallet_address": "LZEjckteAtWrugbsy9zU8VHEZ4iUiXo9Nm",
                                        "balance": 486994.49,
                                        "platform": {
                                            "crypto_id": 2,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 1786142,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 7226,
                                            "price_usd": 7.206011020391402,
                                            "symbol": "INJ",
                                            "name": "Injective"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xdfd5293d8e347dfe59e90efd55b2956a1343963d",
                                        "balance": 232287438454.81,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5994,
                                            "price_usd": 9.265611730463855e-06,
                                            "symbol": "SHIB",
                                            "name": "Shiba Inu"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 129754032.49,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2840,
                                            "price_usd": 0.008262332833125429,
                                            "symbol": "QKC",
                                            "name": "QuarkChain"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbd612a3f30dca67bf60a39fd0d35e39b7ab80774",
                                        "balance": 8545.4,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 4857535.14,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 5279,
                                            "price_usd": 0.11378524797175676,
                                            "symbol": "SOLO",
                                            "name": "Sologenic"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 5000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 1975,
                                            "price_usd": 6.816073415955441,
                                            "symbol": "LINK",
                                            "name": "Chainlink"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x4aefa39caeadd662ae31ab0ce7c8c2c9c0a013e8",
                                        "balance": 6028046.62,
                                        "platform": {
                                            "crypto_id": 5805,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        },
                                        "currency": {
                                            "crypto_id": 5805,
                                            "price_usd": 11.449580596258247,
                                            "symbol": "AVAX",
                                            "name": "Avalanche"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xb38e8c17e38363af6ebdcb3dae12e0243582891d",
                                        "balance": 648737.28,
                                        "platform": {
                                            "crypto_id": 11841,
                                            "symbol": "ARB",
                                            "name": "Arbitrum"
                                        },
                                        "currency": {
                                            "crypto_id": 18852,
                                            "price_usd": 1.0002476884490281,
                                            "symbol": "USDCE",
                                            "name": "USD Coin Bridged"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 7362323.3,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 12687,
                                            "price_usd": 2.070046167587173,
                                            "symbol": "LAZIO",
                                            "name": "S.S. Lazio Fan Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 2017500,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 8891,
                                            "price_usd": 0.330757205392214,
                                            "symbol": "BTCST",
                                            "name": "Bitcoin Standard Hashrate Token"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 931172.14,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 6758,
                                            "price_usd": 0.6827393888036559,
                                            "symbol": "SUSHI",
                                            "name": "SushiSwap"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 187826139,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 24258,
                                            "price_usd": 0.0388400920209194,
                                            "symbol": "UND",
                                            "name": "Unstoppable:DeFi"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 100000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 4758,
                                            "price_usd": 0.03516759240184835,
                                            "symbol": "DF",
                                            "name": "dForce"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 4738878.6,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 1839,
                                            "price_usd": 231.4849911989067,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 13690502.41,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 6669,
                                            "price_usd": 0.2955954734858841,
                                            "symbol": "CVP",
                                            "name": "PowerPool"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 96533701.45,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 24613,
                                            "price_usd": 0.5130654930609977,
                                            "symbol": "EDU",
                                            "name": "Open Campus"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 12678130.28,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4687,
                                            "price_usd": 0.9997721953583942,
                                            "symbol": "BUSD",
                                            "name": "Binance USD"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 750000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7859,
                                            "price_usd": 2.3115699996508043,
                                            "symbol": "BADGER",
                                            "name": "Badger DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 3083.28,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 4023,
                                            "price_usd": 28655.28556241291,
                                            "symbol": "BTCB",
                                            "name": "Bitcoin BEP2"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 40000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 2539,
                                            "price_usd": 0.05087587635660903,
                                            "symbol": "REN",
                                            "name": "Ren"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 181000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8719,
                                            "price_usd": 49.182340809909334,
                                            "symbol": "ILV",
                                            "name": "Illuvium"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1lsmt5a8vqqus5fwslx8pyyemgjtg4y6ugj308t",
                                        "balance": 10825000,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 3714,
                                            "price_usd": 0.05945232953471845,
                                            "symbol": "LTO",
                                            "name": "LTO Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x5a52e96bacdabb82fd05763e25335261b270efcb",
                                        "balance": 190000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7497,
                                            "price_usd": 0.008297742252965251,
                                            "symbol": "POND",
                                            "name": "Marlin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 2377102.24,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 5690,
                                            "price_usd": 1.5999326532552023,
                                            "symbol": "RNDR",
                                            "name": "Render"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",
                                        "balance": 10000000,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 8104,
                                            "price_usd": 0.26931518386189496,
                                            "symbol": "1INCH",
                                            "name": "1inch Network"
                                        }
                                    },
                                    {
                                        "wallet_address": "D7dm1b8DEqaCxcgaPuBXz9FqjAQ7UTK6sz",
                                        "balance": 101528133,
                                        "platform": {
                                            "crypto_id": 74,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        },
                                        "currency": {
                                            "crypto_id": 74,
                                            "price_usd": 0.06803254144522901,
                                            "symbol": "DOGE",
                                            "name": "Dogecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 4229248.91,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7455,
                                            "price_usd": 0.17083954103778173,
                                            "symbol": "AUDIO",
                                            "name": "Audius"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 196136544.06,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 3992,
                                            "price_usd": 0.044512810351528924,
                                            "symbol": "COTI",
                                            "name": "COTI"
                                        }
                                    },
                                    {
                                        "wallet_address": "bnb1u2agwjat20494fmc6jnuau0ls937cfjn4pjwtn",
                                        "balance": 19811,
                                        "platform": {
                                            "crypto_id": 1839,
                                            "symbol": "BNB",
                                            "name": "BNB"
                                        },
                                        "currency": {
                                            "crypto_id": 2,
                                            "price_usd": 75.51196476680965,
                                            "symbol": "LTC",
                                            "name": "Litecoin"
                                        }
                                    },
                                    {
                                        "wallet_address": "0x28c6c06298d514db089934071355e5743bf21d60",
                                        "balance": 619211,
                                        "platform": {
                                            "crypto_id": 1027,
                                            "symbol": "ETH",
                                            "name": "Ethereum"
                                        },
                                        "currency": {
                                            "crypto_id": 7859,
                                            "price_usd": 2.3115699996508043,
                                            "symbol": "BADGER",
                                            "name": "Badger DAO"
                                        }
                                    },
                                    {
                                        "wallet_address": "0xf977814e90da44bfa03b6295a0616a897441acec",
                                        "balance": 4663325,
                                        "platform": {
                                            "crypto_id": 3890,
                                            "symbol": "MATIC",
                                            "name": "Polygon"
                                        },
                                        "currency": {
                                            "crypto_id": 9308,
                                            "price_usd": 3.2036894083443537,
                                            "symbol": "PYR",
                                            "name": "Vulcan Forged PYR"
                                        }
                                    }
                                ]}""")
            return data
        except Exception as e:
            print(e)
