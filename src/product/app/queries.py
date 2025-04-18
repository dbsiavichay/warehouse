from typing import List

from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository


class ProductQueries:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_all(self) -> List[Product]:
        return self.product_repository.get_all()

    def get_by_id(self, id: int) -> Product | None:
        return self.product_repository.get_by_id(id)
