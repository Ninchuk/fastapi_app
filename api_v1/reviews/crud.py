from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.shemas.review import ReviewCreate
from models import User, Review


async def create_review(review: ReviewCreate, db_session: AsyncSession) -> Review:
    review = Review(**review.model_dump())
    db_session.add(review)
    return review
