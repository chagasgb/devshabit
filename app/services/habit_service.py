from datetime import date
from typing import List, Optional
from sqlalchemy.orm import Session
from repositories.habit_repository import HabitRepository
from models import Habito
from habit_schema import HabitCreate, HabitResponse, HabitUpdate

class HabitService:
    def __init__(self, db: Session):
        self.habit_repository = HabitRepository(db)


    def create_habit(self, habit: HabitCreate):
        existing_habit = self.habit_repository.get_by_name(habit.name)
        if existing_habit:
            raise ValueError("O hábito com este nome já existe.")
        
        return self.habit_repository.create(habit)
    
    def update_habit(self, habit: HabitUpdate):
        existing_habit = self.habit_repository.get_by_id(habit.id)
        
        if not existing_habit:
            raise ValueError("Hábito não encontrado.")  
    
        update_data = habit.model_dump(exclude_unset=True)
    
        return self.habit_repository.update(
            habit.id,
            name=update_data.get("name", existing_habit.name),
            description=update_data.get("description", existing_habit.description),
            frequency=update_data.get("frequency", existing_habit.frequency)
        )

