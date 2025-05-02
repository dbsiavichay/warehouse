from typing import Optional

from pydantic import BaseModel


# Inputs
class ProductInput(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category: Optional[str] = None


# Responses
class ProductResponse(ProductInput):
    id: int
