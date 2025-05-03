from src.core.app.repositories import Repository
from src.product.domain.entities import Category, Product


class CategoryRepository(Repository[Category]):
    pass


class ProductRepository(Repository[Product]):
    pass
