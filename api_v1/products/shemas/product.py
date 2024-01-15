from pydantic import BaseModel

from users.schemas.response import Response


class CreateProduct(BaseModel):
    name: str
    description: str
    price: int


class UpdateProduct(CreateProduct):
    pass


class PartialProduct(CreateProduct):
    name: str | None = None
    description: str | None = None
    price: int | None = None
