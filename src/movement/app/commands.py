from src.movement.domain.entities import Movement
from src.movement.domain.repositories import MovementRepository
from src.stock.domain.entities import Stock
from src.stock.domain.repositories import StockRepository


class MovementCommands:
    def __init__(self, movement_repo: MovementRepository, stock_repo: StockRepository):
        self.movement_repo = movement_repo
        self.stock_repo = stock_repo

    def create(self, movement: Movement) -> Movement:
        self.movement_repo.create(movement)
        stock = self.stock_repo.get_by_product_id(movement.product_id)
        if stock is None:
            stock = self.stock_repo.create(Stock.from_movement(movement))
        else:
            stock.update(movement)
            self.stock_repo.update(stock)
        return movement
