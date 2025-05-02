from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.core.domain.entities import Entity


@dataclass
class Product(Entity):
    name: str
    sku: str
    id: Optional[int] = None
    description: Optional[str] = None
    category: Optional[str] = None
    created_at: Optional[datetime] = None
