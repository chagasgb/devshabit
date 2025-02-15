from config.database import SessionLocal, db  
from sqlalchemy.orm import Session
from config.database import Base, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from schemas.habit_schema import HabitCreate, HabitResponse, HabitUpdate
from services.habit_service import HabitService

#cria tabelas
Base.metadata.create_all(bind=db)
app = FastAPI()

#CREATE
@app.post("/", response_model=HabitResponse)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    habit_service = HabitService(db)

    try:
        habit_service.create_habit(habit)
        return HabitResponse(detail="Hábito criado com sucesso!")
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )

#UPDATE
@app.put("/", response_model=HabitResponse)
def update_habit(habit: HabitUpdate, db: Session = Depends(get_db)):
    habit_service = HabitService(db)

    try:
        habit_service.update_habit(habit)
        return HabitResponse(detail="Habito editado com sucesso")
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )