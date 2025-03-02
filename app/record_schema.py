from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import Integer


class RecordCreate(BaseModel):
    habit_id: int
    description: Optional[str] = None


class RecordResponse(BaseModel):
    detail: Optional[str] = None