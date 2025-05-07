from typing import Optional

from pydantic import BaseModel, Field


# Inputs
class CategoryInput(BaseModel):
    name: str
    description: Optional[str] = None


class ProductInput(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category_id: Optional[int] = Field(
        default=None,
        ge=1,
        description="Category ID (must be a positive integer)",
        alias="categoryId",
    )


# Responses
class CategoryResponse(CategoryInput):
    id: int = Field(ge=1, description="Category ID")


class ProductResponse(ProductInput):
    id: int = Field(ge=1, description="Product ID")
