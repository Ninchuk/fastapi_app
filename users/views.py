from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from exceptions.eceptions import UserError
from users import crud
from users.schemas.response import ErrorResponse
from users.schemas.user import CreateUser
from webapp.deps import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/signup/")
async def create_user(
    user: CreateUser,
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> dict:
    try:
        return await crud.create_user(user_in=user, db_session=db_session)
    except UserError as e:
        return jsonable_encoder(ErrorResponse(result="error", message=str(e)))


@router.get("/{username}/")
async def get_user(
    username: str,
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> dict:
    try:
        return await crud.get_user_by_name(username=username, db_session=db_session)
    except UserError as e:
        return jsonable_encoder(ErrorResponse(result="error", message=str(e)))
