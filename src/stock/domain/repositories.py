from abc import ABC, abstractmethod
from typing import List

from src.stock.domain.entities import Stock


class StockRepository(ABC):
    @abstractmethod
    def create(self, stock: Stock) -> Stock:
        raise NotImplementedError

    @abstractmethod
    def update(self, stock: Stock) -> Stock:
        raise NotImplementedError

    @abstractmethod
    def get_by_product_id(self, id: int) -> Stock | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Stock]:
        raise NotImplementedError
