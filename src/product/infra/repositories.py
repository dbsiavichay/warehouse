from typing import List

from sqlalchemy.orm import Session

from src.product.app.repositories import CategoryRepository, ProductRepository
from src.product.domain.entities import Category, Product
from src.product.infra.mappers import CategoryMapper, ProductMapper
from src.product.infra.models import CategoryModel, ProductModel


class CategoryRepositoryImpl(CategoryRepository):
    """Implementation of the CategoryRepository interface using SQLAlchemy
    This class provides methods to interact with the category data in the database
    through SQLAlchemy ORM.
    """

    def __init__(self, session: Session):
        """Initialize the repository with a database session
        Args:
            session (Session): SQLAlchemy database session
        """
        self.session = session

    def create(self, category: Category) -> Category:
        """Creates a new category in the database
        Args:
            category (Category): The category entity to create
        Returns:
            Category: The created category entity
        """
        category_model = CategoryModel(**CategoryMapper.to_dict(category))
        self.session.add(category_model)
        self.session.commit()
        return CategoryMapper.to_entity(category_model)

    def update(self, category: Category) -> Category:
        """Updates an existing category in the database
        Args:
            category (Category): The category entity to update
        Returns:
            Category: The updated category entity
        """
        category_model = self.session.query(CategoryModel).get(category.id)
        for key, value in CategoryMapper.to_dict(category).items():
            setattr(category_model, key, value)
        self.session.commit()
        return CategoryMapper.to_entity(category_model)

    def delete(self, id: int) -> None:
        """Deletes a category by its ID
        Args:
            id (int): The ID of the category to delete
        """
        category = (
            self.session.query(CategoryModel).filter(CategoryModel.id == id).first()
        )
        if category:
            self.session.delete(category)
            self.session.commit()

    def get_all(self) -> List[Category]:
        """Retrieves all categories from the database
        Returns:
            List[Category]: List of all category entities
        """
        categories = self.session.query(CategoryModel).all()
        return [CategoryMapper.to_entity(category) for category in categories]

    def get_by_id(self, id: int) -> Category | None:
        """Retrieves a category by its ID
        Args:
            id (int): The ID of the category to retrieve
        Returns:
            Category | None: The category entity if found, None otherwise
        """
        category = (
            self.session.query(CategoryModel).filter(CategoryModel.id == id).first()
        )
        if category:
            return CategoryMapper.to_entity(category)
        return None


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
