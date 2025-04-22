from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Product:
    name: str
    sku: str
    id: Optional[int] = None
    description: Optional[str] = None
    category: Optional[str] = None
    created_at: Optional[datetime] = None
