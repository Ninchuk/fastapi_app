from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.shemas.review import ReviewCreate
from api_v1.reviews import crud
from webapp.deps import get_db

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_review(
    review: ReviewCreate, db_session: AsyncSession = Depends(get_db)
):
    return await crud.create_review(review=review, db_session=db_session)
