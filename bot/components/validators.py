from pydantic import BaseModel, field_validator, model_validator
from typing import Optional


class OrderRequest(BaseModel):
    """Schema for validating order parameters from user input."""

    symbol: str
    side: str
    order_type: str
    quantity: float
    price: Optional[float] = None
    stop_price: Optional[float] = None

    @field_validator("side")
    @classmethod
    def validate_side(cls, value):
        if value not in ["BUY", "SELL"]:
            raise ValueError("side must be BUY OR SELL")
        return value

    @field_validator("order_type")
    @classmethod
    def validate_type(cls, value):
        if value not in ["MARKET", "LIMIT", "STOP"]:
            raise ValueError("order_type must be MARKET, LIMIT, STOP")
        return value

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, value):
        if value <= 0:
            raise ValueError("quantity must be positive")
        return value

    @model_validator(mode="after")
    def validate_order_prices(self):
        # Ensure required price fields are present for order types that need them.
        if self.order_type == "LIMIT" and self.price is None:
            raise ValueError("price is required for LIMIT order")

        if self.order_type == "STOP" and (
            self.price is None or self.stop_price is None
        ):
            raise ValueError("order type STOP requires both price and stop_price")

        return self
