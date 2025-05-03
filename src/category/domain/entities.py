from dataclasses import dataclass
from typing import Optional

from src.core.domain.entities import Entity


@dataclass
class Category(Entity):
    name: str
    description: Optional[str]
    id: Optional[int] = None
