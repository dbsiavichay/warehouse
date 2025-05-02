from typing import Any, Dict

from src.movement.domain.entities import Movement

from .models import MovementModel


class MovementMapper:
    @staticmethod
    def to_entity(model: MovementModel) -> Movement:
        """Converts an infrastructure model to a domain entity"""
        return Movement(
            id=model.id,
            product_id=model.product_id,
            quantity=model.quantity,
            type=model.type,
            reason=model.reason,
            date=model.date,
        )

    @staticmethod
    def to_dict(entity: Movement) -> Dict[str, Any]:
        """Converts a domain entity to a dictionary for creating a model"""
        result = {
            "product_id": entity.product_id,
            "quantity": entity.quantity,
            "type": entity.type,
            "reason": entity.reason,
            "date": entity.date,
        }

        if entity.id:
            result["id"] = entity.id
        return result
