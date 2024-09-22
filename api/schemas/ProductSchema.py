from pydantic import BaseModel
from datetime import datetime

# Schéma Pydantic pour le modèle Product
class ProductBase(BaseModel):
    url: str

class ProductCreate(ProductBase):
    alert_id: int

class ProductUpdate(ProductBase):
    pass

class ProductInDBBase(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Product(ProductInDBBase):
    alert: 'Alert'
