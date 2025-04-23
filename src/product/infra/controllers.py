from typing import List

from src.product.app.commands import SaveProductCommand
from src.product.app.queries import ProductQueries
from src.product.domain.entities import Product
from src.product.infra.validators import ProductSchema


class ProductController:
    def __init__(
        self, save_product_command: SaveProductCommand, product_queries: ProductQueries
    ):
        self.save_product_command = save_product_command
        self.product_queries = product_queries

    def create(self, new_product: ProductSchema) -> Product:
        product = Product(
            **new_product.model_dump(exclude_none=True),
        )
        return self.save_product_command.execute(product)

    def update(self, id: int, product: ProductSchema) -> Product:
        product = Product(
            id=id,
            **product.model_dump(exclude_none=True),
        )
        return self.save_product_command.execute(product)

    def get_all(self) -> List[Product]:
        return self.product_queries.get_all()

    def get_by_id(self, id: int) -> Product | None:
        return self.product_queries.get_by_id(id)
