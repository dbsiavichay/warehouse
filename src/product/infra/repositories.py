from typing import List

from sqlalchemy.orm import Session

from src.product.domain.entities import Product
from src.product.domain.repositories import ProductRepository
from src.product.infra.models import ProductModel


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Product]:
        products = self.session.query(ProductModel).all()
        return [Product(**product.__dict__) for product in products]

    def get_by_id(self, id: int) -> Product | None:
        product = self.session.query(ProductModel).filter(ProductModel.id == id).first()
        if product:
            return Product(**product.__dict__)
        return None
