from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category: Optional[str] = None
