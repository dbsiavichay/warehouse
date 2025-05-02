from typing import List

from src.product.app.types import ProductOutput

from .repositories import ProductRepository


class ProductQueries:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_all(self) -> List[ProductOutput]:
        products = self.repo.get_all()
        return [product.dict() for product in products]

    def get_by_id(self, id: int) -> ProductOutput | None:
        product = self.repo.get_by_id(id)
        if product is None:
            return None
        return product.dict()
