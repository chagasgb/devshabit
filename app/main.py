from config.database import db  
from sqlalchemy.orm import Session
from config.database import Base, get_db
from fastapi import Depends, FastAPI, HTTPException, status
from typing import List
####

from habit_schema import HabitCreate, HabitResponse, HabitUpdate
from record_schema import RecordCreate, RecordResponse

from services.habit_service import HabitService
from services.record_service import RecordService

from repositories.habit_repository import HabitRepository
from repositories.record_repository import RecordRepository  # Ajuste para o caminho correto

#cria tabelas
Base.metadata.create_all(bind=db)
app = FastAPI()


@app.get("/records")
def get_all(db: Session = Depends(get_db)):
    record_repository = RecordRepository(db)
    return record_repository.get_all()

@app.post("/records", response_model=RecordResponse)
def create_record(record: RecordCreate, db: Session = Depends(get_db)):
    record_service = RecordService(db)
    record_service.create_record(record)
    return RecordResponse(detail=f"Registro criado com sucesso!")


#GET ALL
@app.get("/")
def get_all(db: Session = Depends(get_db)):
    habit_repository = HabitRepository(db)
    return habit_repository.get_all()

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