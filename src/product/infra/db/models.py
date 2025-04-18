from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    sku: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    category: Mapped[Optional[str]] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now()
    )
