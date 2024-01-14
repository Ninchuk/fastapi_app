from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker

from webapp.db import async_session


async def get_db() -> AsyncIterator[async_sessionmaker]:
    async with async_session() as db:
        yield db
        await db.commit()
