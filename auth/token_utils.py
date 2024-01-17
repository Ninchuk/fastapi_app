from datetime import datetime, timedelta

import bcrypt
import jwt

from conf.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.AUTH_JWT.PRIVATE_KEY_PATH.read_text(),
    algorithm: str = settings.AUTH_JWT.ALGORITHM,
    expire_timedelta: timedelta | None = None,
    expire_minutes: int = settings.AUTH_JWT.ACCESS_TOKEN_EXPIRE_MINUTES,
):
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire, iat=now)
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.AUTH_JWT.PUBLIC_KEY_PATH.read_text(),
    algorithm: str = settings.AUTH_JWT.ALGORITHM,
):
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    password_bytes = password.encode()
    return bcrypt.hashpw(password_bytes, salt)


def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password=password.encode(), hashed_password=hashed_password)
