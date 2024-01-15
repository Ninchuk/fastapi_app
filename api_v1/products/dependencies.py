from typing import Annotated

from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products import crud
from models import Product
from webapp.deps import get_db


async def get_product_by_id(
    product_id: Annotated[int, Path],
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> Product:
    product = await crud.get_product(product_id=product_id, db_session=db_session)
    if product:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product id={product_id} not found!",
    )
