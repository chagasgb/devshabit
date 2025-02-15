from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Integer

class HabitCreate(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: List[str]

class HabitUpdate(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[List[str]] = None


class HabitResponse(BaseModel):
    detail: Optional[str] = None
