from dataclasses import dataclass
from typing import Optional

from src.movement.domain.entities import Movement
from src.stock.domain.exceptions import InsufficientStock


@dataclass
class Stock:
    product_id: int
    quantity: int
    id: Optional[int] = None
    location: Optional[str] = None

    @classmethod
    def from_movement(cls, movement: Movement):
        return cls(product_id=movement.product_id, quantity=movement.quantity)

    def update(self, movement: Movement):
        new_quantity = self.quantity + movement.quantity
        if new_quantity < 0:
            raise InsufficientStock(self.product_id, movement.quantity)
        self.quantity = new_quantity
        return self
