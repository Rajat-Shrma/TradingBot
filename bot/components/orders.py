from bot.logging.custom_logging import logging
from bot.exception.custom_exception import CustomException
import sys


def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):

    try:

        logging.info(
            f"Sending Order request | symbol={symbol}, side={side}, type={order_type}, "
            f"qty={quantity}, price={price}, stop_price={stop_price}"
        )
        response = client.create_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        logging.info(f"Order response: {response}")

        return response

    except Exception as e:

        logging.error(f"Order failed: {str(e)}")
        raise CustomException(e, sys)
