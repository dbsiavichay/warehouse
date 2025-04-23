from typing import Any, Dict

from src.stock.domain.entities import Stock
from src.stock.infra.models import StockModel


class StockMapper:
    @staticmethod
    def to_entity(model: StockModel) -> Stock:
        """Converts an infrastructure model to a domain entity"""
        return Stock(
            id=model.id,
            product_id=model.product_id,
            quantity=model.quantity,
            location=model.location,
        )

    @staticmethod
    def to_dict(entity: Stock) -> Dict[str, Any]:
        """Converts a domain entity to a dictionary for creating a model"""
        result = {
            "product_id": entity.product_id,
            "quantity": entity.quantity,
            "location": entity.location,
        }

        # Only include these fields if they are not None
        if entity.id is not None:
            result["id"] = entity.id

        return result
