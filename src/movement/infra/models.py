from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.infra.db import Base
from src.movement.domain.constants import MovementType


class MovementModel(Base):
    __tablename__ = "movements"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int]
    type: Mapped[MovementType]
    reason: Mapped[Optional[str]] = mapped_column(String(128))
    date: Mapped[Optional[datetime]] = mapped_column(default=datetime.now)
    created_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.now)
    product: Mapped["ProductModel"] = relationship(back_populates="movements")
