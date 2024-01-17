from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from api_v1.shemas.token import TokenInfo
from auth import token_utils
from models import User
from users.schemas.user import CreateUser
from webapp.deps import get_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/jwt/login/")


async def get_current_token_payload(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = token_utils.decode_jwt(token=token)
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error",
        )
    return payload


async def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
    db_session: AsyncSession = Depends(get_db),
):
    username = payload.get("name")
    query = select(User).where(User.username == username)
    user = (await db_session.execute(query)).scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid"
        )
    return user


async def get_current_active_auth_user(
    user: CreateUser = Depends(get_current_auth_user),
):
    if user.is_active:
        return user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")


async def validate_user(
    username: str = Form(),
    password: str = Form(),
    db_session: AsyncSession = Depends(get_db),
):
    unauthed = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    query = select(User).where(User.username == username)
    user = (await db_session.execute(query)).scalars().first()
    if not user:
        raise unauthed

    if not token_utils.verify_password(
        password=password, hashed_password=user.password
    ):
        raise unauthed

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )
    return user


@router.post("/login/")
async def auth_user_by_jwt(user: CreateUser = Depends(validate_user)) -> TokenInfo:
    jwt_payload = {"sub": user.id, "name": user.username}
    token = token_utils.encode_jwt(payload=jwt_payload)
    return TokenInfo(access_token=token, token_type="Bearer")


@router.get("/user/me/")
async def check_self_info(
    payload: dict = Depends(get_current_token_payload),
    user: User = Depends(get_current_active_auth_user),
):
    return {"username": user.username, "email": user.email}
