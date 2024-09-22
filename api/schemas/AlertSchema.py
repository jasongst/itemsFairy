from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Schéma Pydantic pour le modèle Alert
class AlertBase(BaseModel):
    provider: str
    session_id: int
    search: str
    status: Optional[int] = 0

class AlertCreate(AlertBase):
    pass

class AlertUpdate(AlertBase):
    status: Optional[int] = None

class AlertInDBBase(AlertBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Alert(AlertInDBBase):
    products: List['Product'] = []
