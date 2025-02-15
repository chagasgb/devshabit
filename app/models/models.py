from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from config.database import Base
from sqlalchemy.sql import func


class Habito(Base):
    __tablename__ = "habitos"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    frequency = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    
#class RegistroHabito(Base):
#    __tablename__ = "registros"
#    id = Column(Integer, primary_key=True)
#    habito_id = Column(Integer, ForeignKey("habitos.id"))
#    timestamp = Column(DateTime, default=func.now())

    
