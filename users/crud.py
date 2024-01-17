import bcrypt
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from exceptions.eceptions import UserError
from models import User
from users.schemas.user import CreateUser, ReturnUser


async def create_user(user_in: CreateUser, db_session: AsyncSession) -> dict:
    query = select(User).where(User.email == user_in.email)
    existing_email = (await db_session.execute(query)).scalars().first()
    if existing_email:
        raise UserError("Email already registered")
    encrypted_password = bcrypt.hashpw(
        user_in.password.encode("utf-8"), bcrypt.gensalt()
    )
    user = User(
        username=user_in.username, email=user_in.email, password=encrypted_password
    )
    db_session.add(user)
    result = {"result": "success", "user": user_in.model_dump()}
    await db_session.commit()
    return result


async def get_user_by_name(username: str, db_session: AsyncSession) -> dict:
    query = select(User).where(User.username == username)
    user = (await db_session.execute(query)).scalars().first()
    if user is None:
        raise UserError("User not found")
    result = ReturnUser(username=user.username, email=user.email)
    return jsonable_encoder(result.model_dump())
