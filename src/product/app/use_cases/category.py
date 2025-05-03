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
