from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime
from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int = Field(primary_key=True)
    username: str = Field(max_length=255, nullable=False)
    email: str = Field(nullable=False, unique=True)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow()))
    password: str
