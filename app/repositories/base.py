from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session

T = TypeVar("T")  # Define um tipo genérico para os modelos

class IRepository(Generic[T]):
    def __init__(self, db: Session, model: T):
        self.db = db
        self.model = model

    def create(self, obj_in) -> T:
        obj = self.model(**obj_in.dict())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, id: int) -> Optional[T]:
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self) -> List[T]:
        return self.db.query(self.model).all()

    def update(self, id: int, obj_in) -> Optional[T]:
        obj = self.get_by_id(id)
        if obj:
            for key, value in obj_in.dict(exclude_unset=True).items():
                setattr(obj, key, value)
            self.db.commit()
            self.db.refresh(obj)
        return obj
