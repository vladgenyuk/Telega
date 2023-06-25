from sqlalchemy import Column, String, Integer, DateTime, func
from database import metadata, Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    username = Column(String(255))
    created_at = Column(DateTime, default=func.now())
