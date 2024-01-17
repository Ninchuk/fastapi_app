from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products import crud
from api_v1.products.dependencies import get_product_by_id
from api_v1.shemas.product import CreateProduct, UpdateProduct, PartialProduct
from models import Product
from webapp.deps import get_db

router = APIRouter()


@router.get("/")
async def get_products(
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> list[Product]:
    return await crud.get_products(db_session=db_session)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product: CreateProduct,
    db_session: Annotated[AsyncSession, Depends(get_db)],
) -> Product:
    return await crud.create_product(product=product, db_session=db_session)


@router.get("/{product_id}/")
async def get_product(
    product: Product = Depends(get_product_by_id),
) -> Product:
    return product


@router.put("/{product_id}/")
async def update_product(
    product_update: UpdateProduct,
    product: Product = Depends(get_product_by_id),
    db_session: AsyncSession = Depends(get_db),
) -> Product:
    return await crud.update_product(
        product=product,
        product_update=product_update,
        db_session=db_session,
    )


@router.patch("/{product_id}/")
async def update_product_partial(
    product_update: PartialProduct,
    product: Product = Depends(get_product_by_id),
    db_session: AsyncSession = Depends(get_db),
) -> Product:
    return await crud.update_product(
        product=product,
        product_update=product_update,
        db_session=db_session,
        partial=True,
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(get_product_by_id),
    db_session: AsyncSession = Depends(get_db),
) -> None:
    await crud.delete_product(product=product, db_session=db_session)
