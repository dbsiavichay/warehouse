from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.infra.db import Base


class StockModel(Base):
    __tablename__ = "stocks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    location: Mapped[Optional[str]] = mapped_column(String(128))

    product: Mapped["ProductModel"] = relationship(  # NOQA: F821
        back_populates="stocks"
    )
