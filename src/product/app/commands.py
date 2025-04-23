from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository


class ProductCommands:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def save(self, product: Product) -> Product:
        return self.repo.save(product)

    def delete(self, id: int) -> None:
        return self.repo.delete(id)
