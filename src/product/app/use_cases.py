from src.product.app.types import ProductInput, ProductOutput
from src.product.domain.entities import Product

from .repositories import ProductRepository


class CreateProductUseCase:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, product_create: ProductInput) -> ProductOutput:
        product = Product(**product_create)
        product = self.repo.create(product)
        return product.dict()


class UpdateProductUseCase:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, id: int, product_update: ProductInput) -> ProductOutput:
        product = Product(id=id, **product_update)
        product = self.repo.update(product)
        return product.dict()


class DeleteProductUseCase:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def execute(self, id: int) -> None:
        return self.repo.delete(id)
