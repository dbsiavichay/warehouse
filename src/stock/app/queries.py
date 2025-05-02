from typing import List

from .repositories import StockRepository
from .types import StockOutput


class StockQueries:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    def get_by_product_id(self, id: int) -> StockOutput | None:
        stock = self.repo.get_by_product_id(id)
        if stock is None:
            return None
        return stock.dict()

    def get_all(self) -> List[StockOutput]:
        stocks = self.repo.get_all()
        return [stock.dict() for stock in stocks]
