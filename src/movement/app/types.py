from typing import NotRequired, TypedDict


class MovementInput(TypedDict):
    product_id: str
    quantity: int
    type: str
    date: NotRequired[str]


class MovementOutput(MovementInput):
    id: int
