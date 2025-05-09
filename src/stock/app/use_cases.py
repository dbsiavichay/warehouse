from typing import List

from src.core.app.repositories import Repository
from src.stock.domain.entities import Stock

from .types import StockOutput


class FilterStocksUseCase:
    def __init__(self, repo: Repository[Stock]):
        self.repo = repo

    def execute(self, **params) -> List[StockOutput]:
        stocks = self.repo.filter_by(**params)
        return [stock.dict() for stock in stocks]
