from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Product:
    id: int
    name: str
    sku: str
    description: Optional[str]
    category: Optional[str]
    created_at: datetime
