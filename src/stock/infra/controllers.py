from typing import List

from src.core.infra.exceptions import NotFoundException
from src.stock.app.queries import StockQueries
from src.stock.infra.validators import StockResponse


class StockController:
    def __init__(self, queries: StockQueries):
        self.queries = queries

    def get_all(self) -> List[StockResponse]:
        stocks = self.queries.get_all()
        return [StockResponse.model_validate(stock) for stock in stocks]

    def get_by_product_id(self, id: int) -> StockResponse:
        stock = self.queries.get_by_product_id(id)
        if stock is None:
            raise NotFoundException("Stock not found")
        return StockResponse.model_validate(stock)
