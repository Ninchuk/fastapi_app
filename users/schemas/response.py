from sqlmodel import SQLModel


class Response(SQLModel):
    result: str = "success"


class ErrorResponse(Response):
    message: str
