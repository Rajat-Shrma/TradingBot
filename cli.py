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
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    try:

        # validate user input using Pydantic
        order = OrderRequest(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price,
        )
        logging.info("Parameter Validation Completed.")

    except Exception as e:
        logging.error(f"Validation error: {e}")
        raise CustomException(e, sys)
    
        # Print order request summary
    print("\nOrder Request")
    print("----------------------")
    print(f"Symbol: {order.symbol}")
    print(f"Side: {order.side}")
    print(f"Order Type: {order.order_type}")
    print(f"Quantity: {order.quantity}")

    if order.order_type == "LIMIT":
        print(f"Price: {order.price}")
    if order.order_type == "STOP":
        print(f"Price: {order.price}")
        print(f"Stop Price: {order.stop_price}")

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
            order.stop_price,
        )

        print("\nOrder Response")
        print("----------------------")
        print("Message: Success")
        if response.get("orderType") == "STOP":
            print(f"Algo ID: {response.get('algoId')}")
        else:
            print(f"Order ID: {response.get('orderId')}")
        
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")
        

    except Exception as e:
        response = {"message": "Failed"}
        print("Order Failed\n")
        print("------------------------")
        print('Message: ', response.get('message'))
        logging.error(f"API error: {e}")
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
