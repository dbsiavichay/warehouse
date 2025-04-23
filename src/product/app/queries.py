from typing import List

from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository


class ProductQueries:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_all(self) -> List[Product]:
        return self.repo.get_all()

    def get_by_id(self, id: int) -> Product | None:
        return self.repo.get_by_id(id)
