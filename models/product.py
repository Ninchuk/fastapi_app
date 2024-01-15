from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TEXT
from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: int = Field(primary_key=True)
    name: str
    description: str = Field(sa_column=Column(TEXT))
    price: int
