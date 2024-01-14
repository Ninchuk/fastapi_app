from uuid import uuid4

from asyncpg import Connection
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from conf.config import settings


class CConnection(Connection):
    def _get_unique_id(self, prefix: str) -> str:
        return f"__asyncpg_{prefix}_{uuid4()}__"


def create_engine() -> AsyncEngine:
    return create_async_engine(
        settings.DB_URL,
        poolclass=NullPool,
        connect_args={
            "connection_class": CConnection,
            "statement_cache_size": 0,
        },
    )


def create_session(engine: AsyncEngine = None) -> async_sessionmaker:
    return async_sessionmaker(
        bind=engine or create_engine(),
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        class_=AsyncSession,
    )


engine = create_engine()
async_session = create_session(engine)
