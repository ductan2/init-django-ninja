from datetime import datetime

from pydantic import BaseModel,ConfigDict



class ProductBase(BaseModel):
    title: str
    description:str
    price : float
    quantity : int

class Product(ProductBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class ProductCreate(ProductBase):
    created_at: datetime
