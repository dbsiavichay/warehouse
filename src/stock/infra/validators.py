from typing import Optional

from pydantic import BaseModel


class StockResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    location: Optional[str] = None
