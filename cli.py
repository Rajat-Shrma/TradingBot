import argparse
import os
import sys
from bot.components.client import BinanceClient
from bot.components.orders import place_order
from bot.components.validators import OrderRequest
from bot.logging.custom_logging import logging
from bot.exception.custom_exception import CustomException


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("SECRET_KEY")


def configure_parser():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot (Improved CLI)"
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)
    return parser


def print_order_request(order):
    print("\nOrder Request")
    print("----------------------")
    print(f"Symbol: {order.symbol}")
    print(f"Side: {order.side}")
    print(f"Order Type: {order.order_type}")
    print(f"Quantity: {order.quantity}")
    if order.order_type in ["LIMIT", "STOP"]:
        print(f"Price: {order.price}")
    if order.order_type == "STOP":
        print(f"Stop Price: {order.stop_price}")


def print_order_response(response):
    print("\nOrder Response")
    print("----------------------")
    print(f"Message: {response.get('message', 'Success')}")
    if response.get("orderType") == "STOP":
        print(f"Algo ID: {response.get('algoId')}")
    else:
        print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Quantity: {response.get('executedQty')}")
    print(f"Average Price: {response.get('avgPrice', 'N/A')}")


def main():
    logging.info("CLI begins")

    parser = configure_parser()
    args = parser.parse_args()

    if not API_KEY or not API_SECRET:
        logging.error(
            "Missing API credentials: API_KEY and/or SECRET_KEY environment variables are not set."
        )
        print("Error: Missing Binance API credentials. Set API_KEY and SECRET_KEY.")
        return 2

    try:
        order = OrderRequest(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price,
        )
        logging.info("Parameter validation completed.")
    except Exception as e:
        logging.error(f"Validation error: {e}")
        print(f"Validation error: {e}")
        return 2

    print_order_request(order)

    try:
        client = BinanceClient(api_key=API_KEY, secret_key=API_SECRET)
        logging.info("BinanceClient created")
        response = place_order(
            client,
            order.symbol,
            order.side,
            order.order_type,
            order.quantity,
            order.price,
            order.stop_price,
        )

        print_order_response(response)
        return 0
    except Exception as e:
        logging.error(f"Order creation failed: {e}")
        print("Order failed. See logs for details.")
        # Keep error details in logs and translate to a custom exception if needed.
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
