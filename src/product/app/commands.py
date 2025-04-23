from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository


class ProductCommands:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def save(self, product: Product) -> Product:
        return self.product_repository.save(product)

    def delete(self, id: int) -> None:
        return self.product_repository.delete(id)
