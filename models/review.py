from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TEXT
from sqlmodel import SQLModel, Field, Relationship


class Review(SQLModel, table=True):
    __tablename__ = "review"

    id: int = Field(primary_key=True)
    title: str = Field(sa_column=Column(String(70)))
    body: str = Field(sa_column=Column(TEXT), default="")
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="reviews")
