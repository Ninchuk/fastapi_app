from collections.abc import AsyncIterator

from sqlalchemy.orm import sessionmaker

from webapp.db import async_session


async def get_db() -> AsyncIterator[sessionmaker]:
    async with async_session() as db:
        yield db
        await db.commit()
