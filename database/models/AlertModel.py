from sqlalchemy import Column, Integer,Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.models.ProductModel import Product
import datetime

from database.database import Base

class Alert(Base):
    __tablename__ = 'alert'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    provider = Column(Text, nullable=False)
    session_id = Column(Integer, nullable=False)
    search = Column(Text, nullable=False)
    status = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now, nullable=False)

    # Relation avec la table Product
    products = relationship('Product', back_populates='alert')
