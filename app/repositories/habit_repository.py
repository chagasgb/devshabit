from typing import List, Optional
from sqlalchemy.orm import Session
from schemas.habit_schema import HabitCreate

from app.models.models import Habito

class HabitRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, habit: HabitCreate):
        habit = Habito(
            name=habit.name,
            description=habit.description,
            frequency=habit.frequency
        )
        self.db.add(habit)
        self.db.commit()
        self.db.refresh(habit)
        return habit
    
    def get_by_id(self, habit_id: int) -> Optional[Habito]:
        return self.db.query(Habito).filter(Habito.id == habit_id).first()
    
    def get_by_name(self, name: str) -> Optional[Habito]:
        return self.db.query(Habito).filter(Habito.name == name).first()

    def get_all(self, user_id: int) -> List[Habito]:
        return self.db.query(Habito).all()   
    
    def update(self, habit_id: int, name: str, description: Optional[str], frequency: str):
        habit = self.get_by_id(habit_id)
        if habit:
            habit.name = name
            habit.description = description
            habit.frequency = frequency
            self.db.commit()
            self.db.refresh(habit)
        return habit
