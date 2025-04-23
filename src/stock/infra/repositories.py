from typing import List

from sqlalchemy.orm import Session

from src.stock.domain.entities import Stock
from src.stock.domain.repositories import StockRepository
from src.stock.infra.models import StockModel

from .mappers import StockMapper


class StockRepositoryImpl(StockRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_product_id(self, id: int) -> Stock | None:
        stock = (
            self.session.query(StockModel).filter(StockModel.product_id == id).first()
        )
        if not stock:
            return Stock(product_id=id, quantity=0)
        return StockMapper.to_entity(stock)

    def get_all(self) -> List[Stock]:
        stocks = self.session.query(StockModel).all()
        return [StockMapper.to_entity(model) for model in stocks]
