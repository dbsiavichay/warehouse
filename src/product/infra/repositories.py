from typing import List

from sqlalchemy.orm import Session

from src.core.infra.repositories import BaseRepository
from src.product.app.repositories import CategoryRepository, ProductRepository
from src.product.domain.entities import Category, Product
from src.product.infra.mappers import ProductMapper
from src.product.infra.models import CategoryModel, ProductModel


class CategoryRepositoryImpl(BaseRepository[Category], CategoryRepository):
    """Implementation of the CategoryRepository interface using SQLAlchemy
    This class provides methods to interact with the category data in the database
    through SQLAlchemy ORM.
    """

    __model__ = CategoryModel


class ProductRepositoryImpl(ProductRepository):
    """Implementation of the ProductRepository interface using SQLAlchemy

    This class provides methods to interact with the product data in the database
    through SQLAlchemy ORM.
    """

    def __init__(self, session: Session):
        """Initialize the repository with a database session

        Args:
            session (Session): SQLAlchemy database session
        """
        self.session = session

    def create(self, product: Product) -> Product:
        """Creates a new product in the database
        Args:
            product (Product): The product entity to create
        Returns:
            Product: The created product entity
        """
        product_model = ProductModel(**ProductMapper.to_dict(product))
        self.session.add(product_model)
        self.session.commit()
        # self.session.refresh(product_model)
        return ProductMapper.to_entity(product_model)

    def update(self, product: Product) -> Product:
        """Updates an existing product in the database
        Args:
            product (Product): The product entity to update
        Returns:
            Product: The updated product entity
        """
        product_model = self.session.query(ProductModel).get(product.id)
        for key, value in ProductMapper.to_dict(product).items():
            setattr(product_model, key, value)
        self.session.commit()
        # self.session.refresh(product_model)
        return ProductMapper.to_entity(product_model)

    def delete(self, id: int) -> None:
        """Deletes a product by its ID
        Args:
            id (int): The ID of the product to delete
        """
        product = self.session.query(ProductModel).filter(ProductModel.id == id).first()

        if product:
            self.session.delete(product)
            self.session.commit()

    def get_all(self) -> List[Product]:
        """Retrieves all products from the database

        Returns:
            List[Product]: List of all product entities
        """
        products = self.session.query(ProductModel).all()
        return [ProductMapper.to_entity(product) for product in products]

    def get_by_id(self, id: int) -> Product | None:
        """Retrieves a product by its ID

        Args:
            id (int): The ID of the product to retrieve

        Returns:
            Product | None: The product entity if found, None otherwise
        """
        product = self.session.query(ProductModel).filter(ProductModel.id == id).first()
        if product:
            return ProductMapper.to_entity(product)
        return None
