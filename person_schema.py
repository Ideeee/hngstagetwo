from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PersonBase(BaseModel):
    name: str
    city: Optional[str] = None


class Person(PersonBase):
    id: int
    date_created: datetime
    last_updated: datetime 

    class Config:
        orm_mode = True