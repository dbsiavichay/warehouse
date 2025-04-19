from typing import List

from src.product.app.queries import ProductQueries
from src.product.domain.entities import Product


class ProductController:
    def __init__(self, product_queries: ProductQueries):
        self.product_queries = product_queries

    def get_all(self) -> List[Product]:
        return self.product_queries.get_all()

    def get_by_id(self, id: int) -> Product | None:
        return self.product_queries.get_by_id(id)
