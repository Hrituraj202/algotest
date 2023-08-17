from .api import ApiService
from .random import apply_random_percentage

api_handler = ApiService()

class ProcessDataService():

    exchanges = ["Binance", "Coinbase", "Kraken", "Bitfinex", "Gemini"]
    exchangeIdMap = {
        "Binance" : 270, 
        "Coinbase" : 89, 
        "Kraken" : 24, 
        "Bitfinex" : 37, 
        "Gemini" : 151
    }

    currencies = ["BTC", "ETH", "USDT", "BNB", "XRP"]
    currencyIdMap = {
        "BTC" : 1, 
        "ETH" : 1027, 
        "USDT" : 825, 
        "BNB" : 1839, 
        "XRP" : 52
    }

    simulateTest = False

    def handle(self, simulateTest):
        try:
            self.simulateTest = simulateTest
            return self.makeCurrencyToExchangeMap()
        except Exception as e:
            print(e)

    def makeExchangeToCurrencyMap(self):
        try:
            processedData = {}
            for exchange in self.exchanges:

                rawData = api_handler.handle(self.exchangeIdMap[exchange], self.simulateTest)["data"]
                for item in rawData:
                    if item["currency"]["symbol"] in self.currencies:
                        if exchange in processedData:
                            price = item["currency"]["price_usd"]
                            if self.simulateTest :
                                price = apply_random_percentage(price)
                            processedData[exchange][item["currency"]["symbol"]] = price
                        else:
                            processedData[exchange] = {}

            return processedData
        except Exception as e:
            print(e)

    def makeCurrencyToExchangeMap(self):
        try:
            processedData = {}
            for exchange in self.exchanges:

                rawData = api_handler.handle(self.exchangeIdMap[exchange], self.simulateTest)["data"]
                for item in rawData:
                    if item["currency"]["symbol"] in self.currencies:
                        if item["currency"]["symbol"] in processedData:
                            price = item["currency"]["price_usd"]
                            if self.simulateTest :
                                price = apply_random_percentage(price)
                            processedData[item["currency"]["symbol"]][exchange] = price
                        else:
                            processedData[item["currency"]["symbol"]] = {}

            return processedData
        except Exception as e:
            print(e)
