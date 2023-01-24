import sqlalchemy
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Table


metadata = sqlalchemy.MetaData()


class File(BaseModel):
    id: int
    file_id: str
    filename: str | None = None


class Item(BaseModel):
    id: int
    title: str
    description: str | None = None


Items = Table(
    "item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
)