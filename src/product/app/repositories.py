from abc import ABC, abstractmethod
from typing import List

from src.product.domain.entities import Product


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def update(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> Product | None:
        raise NotImplementedError
