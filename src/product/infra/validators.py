from typing import Optional

from pydantic import BaseModel


class NewProductSchema(BaseModel):
    name: str
    sku: str
    description: Optional[str] = None
    category: Optional[str] = None
