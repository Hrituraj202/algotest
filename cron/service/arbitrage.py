from .processdata import ProcessDataService
from .algorithm import AlgoService

data_handler = ProcessDataService()
algo_handler = AlgoService()

class ArbitrageService():

    def handle(self, type):
        if type == 1:
            return self.callTwoPointer()
        else:
            return self.callBMFD()

    def callTwoPointer(self):
        simulateTest = True
        processedData = data_handler.handle(simulateTest)
        processedData = algo_handler.handle(processedData)
        return processedData

    def handleThreshold(self, data, threshold):
        try:
            finalData = {}

            for currency, exchange_value_dict in data.items():

                for pair, trade_value in exchange_value_dict.items():
                    if float(trade_value.split(',')[-1]) > float(threshold):
                        finalData[currency] = {pair : trade_value}
            
            return finalData
        except Exception as e:
            print(e)

    def callBMFD(self):

        result = ""

        paths = []

        graph = download()

        for key in graph:
            path = bellman_ford(graph, key)
            if path not in paths and not None:
                paths.append(path)

        for path in paths:
            if path is None:
                result += "No opportunity here :("
                # print("No opportunity here :(")
            else:
                money = 100
                result += f"Starting with {money} in {path[0]} "
                # print(f"Starting with {money} in {path[0]} ")

                for i, value in enumerate(path):
                    if i + 1 < len(path):
                        start = path[i]
                        end = path[i + 1]
                        rate = math.exp(-graph[start][end])
                        money *= rate
                        result += f"{start} to {end} at {rate} = {money}"
                        # print(f"{start} to {end} at {rate} = {money}")
            result += "\n"
            # print("\n")
            return result

    def download():
        
        graph = {}
        # jsrates = api_handler.callExchangeAssets()
        jsrates = json.loads("""{"USD_JPY": "89.1429750", "USD_USD": "1.0000000", "JPY_EUR": "0.0085736", "BTC_USD": "126.7888830", "JPY_BTC": "0.0000916", "USD_EUR": "0.6768007", "EUR_USD": "1.2169689", "EUR_JPY": "124.6882453", "JPY_USD": "0.0110213", "BTC_BTC": "1.0000000", "EUR_BTC": "0.0106548", "BTC_JPY": "12978.8979972", "JPY_JPY": "1.0000000", "BTC_EUR": "93.5226992", "EUR_EUR": "1.0000000", "USD_BTC": "0.0072229"}""")

        pattern = re.compile("([A-Z]{3})_([A-Z]{3})")
        for key in jsrates:
            matches = pattern.match(key)
            conversion_rate = -math.log(float(jsrates[key]))
            from_rate = matches.group(1).encode('ascii', 'ignore')
            to_rate = matches.group(2).encode('ascii', 'ignore')
            if from_rate != to_rate:
                if from_rate not in graph:
                    graph[from_rate] = {}
                graph[from_rate][to_rate] = float(conversion_rate)
        return graph

    # Step 1: For each node prepare the destination and predecessor
    def initialize(graph, source):
        d = {}  # Stands for destination
        p = {}  # Stands for predecessor
        for node in graph:
            d[node] = float('Inf')  # We start admiting that the rest of nodes are very very far
            p[node] = None
        d[source] = 0  # For the source we know how to reach
        return d, p

    def relax(node, neighbour, graph, d, p):
        # If the distance between the node and the neighbour is lower than the one I have now
        if d[neighbour] > d[node] + graph[node][neighbour]:
            # Record this lower distance
            d[neighbour] = d[node] + graph[node][neighbour]
            p[neighbour] = node

    def retrace_negative_loop(p, start):
        arbitrageLoop = [start]
        next_node = start
        while True:
            next_node = p[next_node]
            if next_node not in arbitrageLoop:
                arbitrageLoop.append(next_node)
            else:
                arbitrageLoop.append(next_node)
                arbitrageLoop = arbitrageLoop[arbitrageLoop.index(next_node):]
                return arbitrageLoop

    def bellman_ford(graph, source):
        d, p = initialize(graph, source)
        for i in range(len(graph) - 1):  # Run this until is converges
            for u in graph:
                for v in graph[u]:  # For each neighbour of u
                    relax(u, v, graph, d, p)  # Lets relax it

        # Step 3: check for negative-weight cycles
        for u in graph:
            for v in graph[u]:
                if d[v] < d[u] + graph[u][v]:
                    return retrace_negative_loop(p, source)
        return None
