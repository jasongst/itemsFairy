from sqlalchemy.orm import Session
from fastapi import Depends

from api.schemas import ProductSchema
from database.models import ProductModel
from database.database import get_db_connection

class AlertRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db
    
    def create(self, product: ProductSchema.ProductCreate):
        db_product = ProductModel.Product(**product.dict(), alert_id=alert_id)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product