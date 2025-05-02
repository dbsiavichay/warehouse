from typing import NotRequired, TypedDict


class ProductBase(TypedDict):
    name: str
    sku: str
    description: NotRequired[str]
    category: NotRequired[str]


class ProductInput(ProductBase):
    pass


class ProductOutput(ProductBase):
    id: int
