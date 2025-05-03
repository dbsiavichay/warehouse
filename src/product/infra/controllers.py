from typing import List

from src.core.infra.exceptions import NotFoundException
from src.product.app.queries import ProductQueries
from src.product.app.use_cases import (
    CreateCategoryUseCase,
    CreateProductUseCase,
    DeleteCategoryUseCase,
    DeleteProductUseCase,
    UpdateCategoryUseCase,
    UpdateProductUseCase,
)
from src.product.domain.entities import Product
from src.product.infra.validators import (
    CategoryInput,
    CategoryResponse,
    ProductInput,
    ProductResponse,
)


class CategoryController:
    def __init__(
        self,
        create_category: CreateCategoryUseCase,
        update_category: UpdateCategoryUseCase,
        delete_category: DeleteCategoryUseCase,
    ):
        self.create_category = create_category
        self.update_category = update_category
        self.delete_category = delete_category

    def create(self, new_category: CategoryInput) -> CategoryResponse:
        category = self.create_category.execute(
            new_category.model_dump(exclude_none=True)
        )
        return CategoryResponse.model_validate(category)

    def update(self, id: int, category: CategoryInput) -> Product:
        category = self.update_category.execute(
            id, category.model_dump(exclude_none=True)
        )
        return CategoryResponse.model_validate(category)

    def delete(self, id: int) -> None:
        self.delete_category.execute(id)


class ProductController:
    def __init__(
        self,
        create_product: CreateProductUseCase,
        update_product: UpdateProductUseCase,
        delete_product: DeleteProductUseCase,
        product_queries: ProductQueries,
    ):
        self.create_product = create_product
        self.update_product = update_product
        self.delete_product = delete_product
        self.product_queries = product_queries

    def create(self, new_product: ProductInput) -> ProductResponse:
        product = self.create_product.execute(new_product.model_dump(exclude_none=True))
        return ProductResponse.model_validate(product)

    def update(self, id: int, product: ProductInput) -> Product:
        product = self.update_product.execute(id, product.model_dump(exclude_none=True))
        return ProductResponse.model_validate(product)

    def delete(self, id: int) -> None:
        self.delete_product.execute(id)

    def get_all(self) -> List[ProductResponse]:
        products = self.product_queries.get_all()
        return [ProductResponse.model_validate(product) for product in products]

    def get_by_id(self, id: int) -> ProductResponse:
        product = self.product_queries.get_by_id(id)
        if product is None:
            raise NotFoundException("Product not found")
        return ProductResponse.model_validate(product)
