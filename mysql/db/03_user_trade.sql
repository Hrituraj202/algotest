INSERT INTO user (email, first_name, last_name, password_hash) VALUES ('rituraj202@gmail.com', 'Rituraj', 'Singh', '$2b$12$MXwQFgQQj2tkZ9tdbCRobeVjmzBnDvrs2nHRSpNXAedg9AlgPCWm2'), ('hrituraj202@gmail.com', 'Ritu', 'Raj', '$2b$12$hMiToZirK5uxhNr7g8myXevOW7iJJua6JQKXieEtackwSKQKgXHMu');
INSERT INTO trade (user_id, asset, exchanges, profit_percent, timestamp) VALUES (1, 'BTC', '{"exchange1": {"name": "Coinbase", "currency": "USD"}, "exchange2": {"name": "Binance", "currency": "USDT"}}', 10.5, '2023-08-16 12:34:56'), (2, 'ETH', '{"exchange1": {"name": "Kraken", "currency": "EUR"}, "exchange2": {"name": "Bitfinex", "currency": "USD"}}', 5.2, '2023-08-17 08:15:23'), (2, 'LTC', '{"exchange1": {"name": "Bittrex", "currency": "BTC"}, "exchange2": {"name": "Huobi", "currency": "USDT"}}', 8.9, '2023-08-18 16:45:12'), (2, 'XRP', '{"exchange1": {"name": "Poloniex", "currency": "USDT"}, "exchange2": {"name": "Coinbase Pro", "currency": "USD"}}', 0.3, '2023-08-19 22:01:34');