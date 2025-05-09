from typing import Any, Dict, Optional

from src.core.infra.mappers import Mapper
from src.product.domain.entities import Category, Product
from src.product.infra.models import CategoryModel, ProductModel


class CategoryMapper(Mapper[Category, CategoryModel]):
    def to_entity(self, model: Optional[CategoryModel]) -> Optional[Category]:
        """Converts an infrastructure model to a domain entity"""
        if not model:
            return None

        return Category(
            id=model.id,
            name=model.name,
            description=model.description,
        )

    def to_dict(self, entity: Category) -> Dict[str, Any]:
        """Converts a domain entity to a dictionary for creating a model"""
        # Exclude id and created_at if they are None (for creation)
        result = {
            "name": entity.name,
            "description": entity.description,
        }
        # Only include these fields if they are not None
        if entity.id is not None:
            result["id"] = entity.id
        # We don't include created_at in the dictionary as it's automatically set
        # in the model with default=datetime.now
        return result


class ProductMapper(Mapper[Product, ProductModel]):
    def to_entity(self, model: Optional[ProductModel]) -> Optional[Product]:
        """Converts an infrastructure model to a domain entity"""
        if not model:
            return None

        return Product(
            id=model.id,
            name=model.name,
            sku=model.sku,
            description=model.description,
            category_id=model.category_id,
            created_at=model.created_at,
        )

    def to_dict(self, entity: Product) -> Dict[str, Any]:
        """Converts a domain entity to a dictionary for creating a model"""
        # Exclude id and created_at if they are None (for creation)
        result = {
            "name": entity.name,
            "sku": entity.sku,
            "description": entity.description,
            "category_id": entity.category_id,
        }

        # Only include these fields if they are not None
        if entity.id is not None:
            result["id"] = entity.id

        # We don't include created_at in the dictionary as it's automatically set
        # in the model with default=datetime.now

        return result
