from src.core.infra.repositories import BaseRepository
from src.product.domain.entities import Category, Product
from src.product.infra.models import CategoryModel, ProductModel


class CategoryRepositoryImpl(BaseRepository[Category]):
    """Implementation of the CategoryRepository interface using SQLAlchemy
    This class provides methods to interact with the category data in the database
    through SQLAlchemy ORM.
    """

    __model__ = CategoryModel


class ProductRepositoryImpl(BaseRepository[Product]):
    """Implementation of the ProductRepository interface using SQLAlchemy

    This class provides methods to interact with the product data in the database
    through SQLAlchemy ORM.
    """

    __model__ = ProductModel
