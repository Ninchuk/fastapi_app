from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    __tablename__ = "product"

    id: int = Field(primary_key=True)
    name: str
    description: str
    price: int
