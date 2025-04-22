from typing import Any, Dict

from src.product.domain.entities import Product
from src.product.infra.models import ProductModel


class ProductMapper:
    @staticmethod
    def to_entity(model: ProductModel) -> Product:
        """Converts an infrastructure model to a domain entity"""
        return Product(
            id=model.id,
            name=model.name,
            sku=model.sku,
            description=model.description,
            category=model.category,
            created_at=model.created_at,
        )

    @staticmethod
    def to_dict(entity: Product) -> Dict[str, Any]:
        """Converts a domain entity to a dictionary for creating a model"""
        # Exclude id and created_at if they are None (for creation)
        result = {
            "name": entity.name,
            "sku": entity.sku,
            "description": entity.description,
            "category": entity.category,
        }

        # Only include these fields if they are not None
        if entity.id is not None:
            result["id"] = entity.id

        # We don't include created_at in the dictionary as it's automatically set
        # in the model with default=datetime.now

        return result
