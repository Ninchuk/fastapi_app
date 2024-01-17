from pydantic import BaseModel


class ReviewCreate(BaseModel):
    title: str
    body: str
    user_id: int
