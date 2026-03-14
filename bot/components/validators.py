from pydantic import BaseModel, field_validator, model_validator
from typing import Optional

# Pydantic Model to Validate the user input.


class OrderRequest(BaseModel):

    symbol: str
    side: str
    order_type: str
    quantity: float
    price: Optional[float] = None

    @field_validator("side")
    @classmethod
    def validate_side(cls, value):
        if value not in ["BUY", "SELL"]:
            raise ValueError("side must be BUY or SELL")
        return value

    @field_validator("order_type")
    @classmethod
    def validate_type(cls, value):
        if value not in ["MARKET", "LIMIT"]:
            raise ValueError("order_type must be MARKET or LIMIT")
        return value

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, value):
        if value <= 0:
            raise ValueError("quantity must be positive")
        return value

    @model_validator(mode="after")
    def validate_limit_price(self):

        if self.order_type == "LIMIT" and self.price is None:
            raise ValueError("price is required for LIMIT order")

        return self
