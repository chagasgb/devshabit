from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.models import Habito

class RecordRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, name: str, description: Optional[str], frequency: list) -> Habito:
        habit = Habito(
            name=name,
            description=description,
            frequency=frequency
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
    
    
    def update(self, habit_id: int, update_data: dict) -> Optional[Habito]:
        habit = self.get(habit_id)
        if not habit:
            return None  # Retorna None se o hábito não existir
    
        # Atualiza apenas os campos presentes no update_data
        for key, value in update_data.items():
            if value is not None:  # Evita sobrescrever com None
                setattr(habit, key, value)
    
        self.db.commit()
        self.db.refresh(habit)
        return habit
  