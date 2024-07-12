from pydantic import Field
from src.schemas.base import BaseSchemaMixIn


class ProductIn(BaseSchemaMixIn):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product status")
