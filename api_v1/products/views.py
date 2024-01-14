from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products import crud
from api_v1.products.shemas.product import CreateProduct
from webapp.deps import get_db

router = APIRouter()


@router.get("/")
async def get_products(
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    return await crud.get_products(db_session=db_session)


@router.post("/")
async def create_product(
    product: CreateProduct,
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    return await crud.create_product(product=product, db_session=db_session)


@router.get("/{product_id}/")
async def get_product(
    product_id: int,
    db_session: Annotated[AsyncSession, Depends(get_db)],
):
    product = await crud.get_product(product_id=product_id, db_session=db_session)
    if product:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product id={product_id} not found!",
    )
