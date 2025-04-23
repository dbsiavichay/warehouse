from typing import List

from fastapi import APIRouter, Depends

from src import get_stock_controller
from src.stock.domain.entities import Stock

from .controllers import StockController


class StockRouter:
    def __init__(self):
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self):
        """Sets up all the routes for the router."""
        self.router.get(
            "/{product_id}", response_model=Stock, summary="Get stock by product_id"
        )(self.get_by_product_id)
        self.router.get("", response_model=List[Stock], summary="Get all stocks")(
            self.get_all
        )

    def get_by_product_id(
        self,
        product_id: int,
        controller: StockController = Depends(get_stock_controller),
    ):
        """Gets a stock by product_id."""
        return controller.get_by_product_id(product_id)

    def get_all(self, controller: StockController = Depends(get_stock_controller)):
        """Gets all products stock."""
        return controller.get_all()
