from pydantic import BaseModel

from users.schemas.response import Response


class CreateProduct(BaseModel):
    name: str
    description: str
    price: int


class ReturnProduct(Response):
    name: str
    description: str
    price: int
