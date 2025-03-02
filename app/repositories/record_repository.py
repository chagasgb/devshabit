from typing import List, Optional
from sqlalchemy.orm import Session

from record_schema import RecordCreate
from models import RecordHabit

class RecordRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, record: RecordCreate):
        
        new_record = RecordHabit(
            habit_id=record.habit_id,
            description=record.description,
        )
        self.db.add(new_record)
        self.db.commit()
        self.db.refresh(new_record)
    
    def get_all(self) -> List[RecordHabit]:
        return self.db.query(RecordHabit).all()   
