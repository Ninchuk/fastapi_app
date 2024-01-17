from sqlmodel import SQLModel, Field


class Token(SQLModel, table=True):
    __tablename__ = "token"

    public_address: str = Field(primary_key=True, unique=True, nullable=False)
