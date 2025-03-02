from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func


class Habito(Base):
    __tablename__ = "habitos"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    frequency = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    
class RecordHabit(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    habit_id = Column(Integer, ForeignKey("habitos.id"), nullable=False)  # 🔥 ForeignKey
    description = Column(String, nullable=True)
    recorded_at = Column(DateTime, default=func.now())
    
