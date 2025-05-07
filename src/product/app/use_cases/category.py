from typing import Optional

from src.product.app.repositories import CategoryRepository
from src.product.app.types import CategoryInput, CategoryOutput
from src.product.domain.entities import Category


class CreateCategoryUseCase:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, category_create: CategoryInput) -> CategoryOutput:
        category = Category(**category_create)
        category = self.repo.create(category)
        return category.dict()


class UpdateCategoryUseCase:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, id: int, category_update: CategoryInput) -> CategoryOutput:
        category = Category(id=id, **category_update)
        category = self.repo.update(category)
        return category.dict()


class DeleteCategoryUseCase:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, id: int) -> None:
        self.repo.delete(id)


class GetAllCategoriesUseCase:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self) -> list[CategoryOutput]:
        categories = self.repo.get_all()
        return [category.dict() for category in categories]


class GetCategoryUseCase:
    def __init__(self, repo: CategoryRepository):
        self.repo = repo

    def execute(self, id: int) -> Optional[CategoryOutput]:
        category = self.repo.get_by_id(id)
        if category is None:
            return None
        return category.dict()
