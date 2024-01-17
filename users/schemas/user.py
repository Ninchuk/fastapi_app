from pydantic import BaseModel, EmailStr, ConfigDict

from users.schemas.response import Response


class CreateUser(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    email: EmailStr
    password: str
    is_active: bool = True


class ReturnUser(Response):
    username: str
    email: str
