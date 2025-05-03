from typing import Optional

from pydantic import BaseModel


# Inputs
class CategoryInput(BaseModel):
    name: str
    description: Optional[str] = None


class ProductInput(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category: Optional[str] = None


# Responses
class CategoryResponse(CategoryInput):
    id: int


class ProductResponse(ProductInput):
    id: int
