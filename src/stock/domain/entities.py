from dataclasses import dataclass
from typing import Optional

from src.core.domain.entities import Entity
from src.stock.domain.exceptions import InsufficientStock


@dataclass
class Stock(Entity):
    product_id: int
    quantity: int
    id: Optional[int] = None
    location: Optional[str] = None

    def update_quantity(self, quantity: int):
        new_quantity = self.quantity + quantity
        if new_quantity < 0:
            raise InsufficientStock(self.product_id, quantity)
        self.quantity = new_quantity
        return self
