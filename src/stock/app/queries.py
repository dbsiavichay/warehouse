from typing import List

from src.stock.domain.entities import Stock
from src.stock.domain.repositories import StockRepository


class StockQueries:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    def get_by_product_id(self, id: int) -> Stock | None:
        return self.repo.get_by_product_id(id)

    def get_all(self) -> List[Stock]:
        return self.repo.get_all()
