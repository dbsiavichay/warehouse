from typing import Any, Dict, Optional

from src.core.infra.mappers import Mapper
from src.stock.domain.entities import Stock
from src.stock.infra.models import StockModel


class StockMapper(Mapper[Stock, StockModel]):
    def to_entity(self, model: Optional[StockModel]) -> Optional[Stock]:
        """Converts an infrastructure model to a domain entity"""
        if model is None:
            return None

        return Stock(
            id=model.id,
            product_id=model.product_id,
            quantity=model.quantity,
            location=model.location,
        )

    def to_dict(self, entity: Stock) -> Dict[str, Any]:
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
