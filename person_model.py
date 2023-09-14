import datetime as dt
from enum import Enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, Enum, Text, String, DateTime, ARRAY
from sqlalchemy.orm import relationship

from db.db_setup import Base

class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    city = Column(String(100))
    date_created = Column(DateTime, default=dt.datetime.utcnow)
    last_updated = Column(DateTime, default=dt.datetime.utcnow)