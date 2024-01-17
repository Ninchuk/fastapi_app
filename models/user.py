from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel, Relationship


if TYPE_CHECKING:
    from .profile import Profile
    from .review import Review
    from .token import Token


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int = Field(primary_key=True)
    username: str = Field(max_length=255, nullable=False, unique=True)
    email: str = Field(nullable=False, unique=True)
    is_active: bool = Field(nullable=False, default=True)
    public_address: str = Field(foreign_key="token.public_address", nullable=True)
    token: "Token" = Relationship()
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), nullable=False, default=datetime.utcnow()
        )
    )
    password: bytes
    reviews: list["Review"] = Relationship(back_populates="user")
    profile: "Profile" = Relationship(back_populates="user")
