class AlgoService():

    def handle(self, data):
        try:
            finalData = {}

            for currency, exchange_values in data.items():

                pairs = []
                stack = []

                # exchange_values.items() produce tuples
                sorted_exchanges = sorted(exchange_values.items(), key=lambda item: item[1])

                for exchange, value in sorted_exchanges:
                    while stack and exchange_values[stack[-1]] < value:
                        i = stack.pop()
                        pairs.append((i, exchange))

                    stack.append(exchange)

                result_dict = {}
                for pair in pairs:
                    value1 = exchange_values[pair[0]]
                    value2 = exchange_values[pair[1]]
                    key = f"{pair[0]},{pair[1]}"
                    result_dict[key] = f"{value1},{value2},{value2-value1}"
                
                finalData[currency] = result_dict

            return finalData
        except Exception as e:
            print(e)