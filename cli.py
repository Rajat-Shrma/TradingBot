import argparse
from bot.components.client import BinanceClient
from bot.components.orders import place_order
from bot.components.validators import OrderRequest
from bot.logging.custom_logging import logging
from bot.exception.custom_exception import CustomException
import sys
import os

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("SECRET_KEY")


def main():
    logging.info("Begins")
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        # validate user input using Pydantic
        order = OrderRequest(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
        logging.info("Parameter Validation Completed.")

    except Exception as e:
        logging.error(f"Validation error: {e}")
        raise CustomException(e, sys)

    try:

        client = BinanceClient(api_key=API_KEY, secret_key=API_SECRET)
        logging.info("Binance Client object Created.")
        response = place_order(
            client,
            order.symbol,
            order.side,
            order.order_type,
            order.quantity,
            order.price,
        )

        api_response = {
            "request": "success",
            "orderId": response["orderId"],
            "symbol": response["symbol"],
            "status": response["status"],
        }
        print("API Response: ", api_response)

    except Exception as e:

        print("\nOrder execution failed")

        logging.error(f"API error: {e}")
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
