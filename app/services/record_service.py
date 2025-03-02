from datetime import date
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from repositories.habit_repository import HabitRepository
from repositories.record_repository import  RecordRepository
from models import Habito
from record_schema import RecordCreate

class RecordService:
    def __init__(self, db: Session):
        self.habit_repository = HabitRepository(db)
        self.record_repository = RecordRepository(db)


    def create_record(self, record: RecordCreate):
        existing_habit = self.habit_repository.get_by_id(record.habit_id)
        
        if not existing_habit:
            raise HTTPException(status_code=400, detail="O hábito com este ID não existe.")

        return self.record_repository.create(record)