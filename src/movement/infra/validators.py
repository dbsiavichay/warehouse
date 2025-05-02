from typing import Optional

from pydantic import BaseModel, field_validator, model_validator

from src.movement.domain.constants import MovementType
from src.movement.domain.exceptions import InvalidMovementTypeException


class MovementBase(BaseModel):
    product_id: int
    quantity: int
    type: MovementType
    reason: Optional[str] = None


class MovementInput(MovementBase):
    @field_validator("quantity", mode="after")
    @classmethod
    def validate_quantity_not_zero(cls, v):
        if v == 0:
            raise InvalidMovementTypeException("La cantidad no puede ser cero")
        return v

    @model_validator(mode="after")
    def validate_quantity_by_movement_type(self) -> "MovementSchema":
        if self.type == MovementType.IN and self.quantity < 0:
            raise InvalidMovementTypeException(
                "La cantidad debe ser positiva para movimientos de entrada"
            )
        elif self.type == MovementType.OUT and self.quantity > 0:
            raise InvalidMovementTypeException(
                "La cantidad debe ser negativa para movimientos de salida"
            )
        return self


class MovementResponse(MovementBase):
    id: int
