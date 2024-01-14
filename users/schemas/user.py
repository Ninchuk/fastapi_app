from pydantic import BaseModel, EmailStr

from users.schemas.response import Response


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class ReturnUser(Response):
    username: str
    email: str
