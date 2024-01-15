from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TEXT
from sqlmodel import SQLModel, Field, Relationship


class Review(SQLModel, table=True):
    __tablename__ = "review"

    id: int = Field(primary_key=True)
    title: str = Field(max_length=70)
    body: str = Field(sa_column=Column(TEXT), default="")
    user_id: int = Field(foreign_key="user.id", nullable=False)
    user: "User" = Relationship()
