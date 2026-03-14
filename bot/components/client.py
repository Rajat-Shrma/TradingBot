from binance.client import Client


class BinanceClient:

    def __init__(self, api_key, secret_key):
        self.client = Client(api_key=api_key, api_secret=secret_key)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self.client.futures_create_order(**params)
