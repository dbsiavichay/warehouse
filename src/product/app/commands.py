from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository


class SaveProductCommand:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, product: Product) -> Product:
        return self.product_repository.save(product)
