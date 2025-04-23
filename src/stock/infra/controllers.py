from typing import List

from src.stock.app.queries import StockQueries
from src.stock.domain.entities import Stock


class StockController:
    def __init__(self, queries: StockQueries):
        self.queries = queries

    def get_all(self) -> List[Stock]:
        return self.queries.get_all()

    def get_by_product_id(self, id: int) -> Stock | None:
        return self.queries.get_by_product_id(id)
