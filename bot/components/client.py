from binance.client import Client


class BinanceClient:

    def __init__(self, api_key, secret_key):
        self.client = Client(api_key=api_key, api_secret=secret_key)

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(
        self, symbol, side, order_type, quantity, price=None, stop_price=None
    ):
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity,
        }

        # For limit orders, we must supply a price and time-in-force.
        if order_type.upper() == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        # For stop orders, set trigger price and price as required by Binance API.
        if order_type.upper() == "STOP":
            params["price"] = price
            params["triggerprice"] = stop_price
            params["timeInForce"] = "GTC"

        # Send the create order request to Binance futures API
        return self.client.futures_create_order(**params)
