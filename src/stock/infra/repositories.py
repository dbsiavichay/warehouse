from src.core.infra.repositories import BaseRepository
from src.stock.domain.entities import Stock
from src.stock.infra.models import StockModel


class StockRepositoryImpl(BaseRepository[Stock]):
    __model__ = StockModel
