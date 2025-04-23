from dataclasses import dataclass
from typing import Optional


@dataclass
class Stock:
    product_id: int
    quantity: int
    id: Optional[int] = None
    location: Optional[str] = None
