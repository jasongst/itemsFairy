from sqlalchemy.orm import Session
from fastapi import Depends

from api.schemas import AlertSchema
from database.models import AlertModel
from database.database import get_db_connection

class AlertRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(self, skip: int = 0, limit: int = 100):
        return self.db.query(AlertModel.Alert).offset(skip).limit(limit).all()
    
    def get(self, alert_id: int):
        return self.db.query(AlertModel.Alert).filter(AlertModel.Alert.id == alert_id).first()
    
    def get_by_session_id(self, session_id: int):
        return self.db.query(AlertModel.Alert).filter(AlertModel.Alert.session_id == session_id).first()
    
    def create(self, alert: AlertSchema.AlertCreate):
        db_alert = AlertModel.Alert(**alert.dict())
        self.db.add(db_alert)
        self.db.commit()
        self.db.refresh(db_alert)
        return db_alert