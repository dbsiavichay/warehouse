from typing import List

from sqlalchemy.orm import Session

from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository
from src.product.infra.mappers import ProductMapper
from src.product.infra.models import ProductModel


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

    def save(self, product: Product) -> Product:
        """Saves a product entity to the database

        This method handles both creation of new products and updates to existing ones.
        If the product has no ID, it will be created as a new record.
        If the product has an ID, the existing record will be updated.

        Args:
            product (Product): The product entity to save

        Returns:
            Product: The saved product entity with updated information
        """
        # Convert entity to dictionary for the model
        product_dict = ProductMapper.to_dict(product)

        # If it's a new product (without ID)
        if product.id is None:
            product_model = ProductModel(**product_dict)
            self.session.add(product_model)
        else:
            # If it's an update
            product_model = self.session.query(ProductModel).get(product.id)
            for key, value in product_dict.items():
                setattr(product_model, key, value)

        self.session.commit()

        # Convert the model back to domain entity
        return ProductMapper.to_entity(product_model)

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

    def delete(self, id: int) -> None:
        """Deletes a product by its ID
        Args:
            id (int): The ID of the product to delete
        """
        product = self.session.query(ProductModel).filter(ProductModel.id == id).first()

        if product:
            self.session.delete(product)
            self.session.commit()
