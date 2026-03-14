from bot.logging.custom_logging import logging
from bot.exception.custom_exception import CustomException
import sys


def place_order(client, symbol, side, order_type, quantity, price=None):

    try:

        logging.info(f"Sending order request: {symbol} {side} {order_type}")

        response = client.create_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        logging.info(f"Order response: {response}")

        return response

    except Exception as e:

        logging.error(f"Order failed: {str(e)}")
        raise CustomException(e, sys)
