from datetime import datetime
from typing import Optional

from pydantic import AliasChoices, BaseModel, Field, field_validator, model_validator

from src.core.infra.validators import QueryParams
from src.movement.domain.constants import MovementType
from src.movement.domain.exceptions import InvalidMovementTypeException


class MovementBase(BaseModel):
    product_id: int = Field(
        ...,
        ge=1,
        description="Product ID",
        validation_alias=AliasChoices("productId", "product_id"),
        serialization_alias="productId",
    )
    quantity: int = Field(..., ge=1, description="Quantity")
    type: MovementType
    reason: Optional[str] = None
    date: Optional[datetime] = None


class MovementInput(MovementBase):
    @field_validator("quantity", mode="after")
    @classmethod
    def validate_quantity_not_zero(cls, v):
        if v == 0:
            raise InvalidMovementTypeException("La cantidad no puede ser cero")
        return v

    @model_validator(mode="after")
    def validate_quantity_by_movement_type(self) -> "MovementInput":
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


class MovementQueryParams(QueryParams):
    product_id: Optional[int] = Field(
        None,
        ge=1,
        alias="productId",
    )
    type: Optional[MovementType] = None
    from_date: Optional[datetime] = Field(None, alias="fromDate")
    to_date: Optional[datetime] = Field(None, alias="toDate")
