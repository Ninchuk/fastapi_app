from sqlmodel import SQLModel, Field, Relationship


class Profile(SQLModel, table=True):
    __tablename__ = "profile"

    id: int = Field(primary_key=True)
    first_name: str | None
    last_name: str | None
    about_me: str | None
    user_id: int = Field(foreign_key="user.id", unique=True)
    user: "User" = Relationship(back_populates="profile")
