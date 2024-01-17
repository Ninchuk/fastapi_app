from pathlib import Path
from typing import List, Union

from pydantic import field_validator, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    PRIVATE_KEY_PATH: Path = BASE_DIR / "certs" / "private_key.pem"
    PUBLIC_KEY_PATH: Path = BASE_DIR / "certs" / "public_key.pem"
    ALGORITHM: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15


class Settings(BaseSettings):
    BIND_IP: str = "0.0.0.0"
    BIND_PORT: int = 8000
    WEB_CONCURRENCY: int = 1

    DB_LEVEL_SIZE: int = 100
    DB_LEVELS_COUNT: int = 3
    DB_POOL_SIZE: int = 50
    DB_MAX_OVERFLOW: int = 99
    DB_ECHO: bool = False
    DB_URL: str
    DB_TIMEOUT: int = 5
    ALEMBIC_MIGRATION_VERSION_TABLE: str = "migration_version"

    BACKEND_CORS_ORIGINS: List = []

    api_v1_prefix: str = "/api/v1"
    AUTH_JWT: AuthJWT = AuthJWT()
    PASSWORD_LEN: int = 15
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("BACKEND_CORS_ORIGINS")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
