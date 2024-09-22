from sqlalchemy import Column, Integer,Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

from database.database import Base

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    alert_id = Column(Integer, ForeignKey('alert.id'), nullable=False)
    url = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    # Relation avec la table Alert
    alert = relationship('Alert', back_populates='products')
