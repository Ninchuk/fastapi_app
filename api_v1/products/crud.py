from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from api_v1.shemas.product import CreateProduct, UpdateProduct, PartialProduct
from models import Product


async def create_product(product: CreateProduct, db_session: AsyncSession) -> Product:
    product = Product(**product.model_dump())
    db_session.add(product)
    await db_session.commit()
    await db_session.refresh(product)
    return product


async def get_products(db_session: AsyncSession) -> list[Product]:
    query = select(Product).order_by(Product.id)
    products = (await db_session.execute(query)).scalars().all()
    return list(products)


async def get_product(product_id: int, db_session: AsyncSession) -> Product | None:
    return await db_session.get(Product, product_id)


async def update_product(
    product: Product,
    product_update: UpdateProduct | PartialProduct,
    db_session: AsyncSession,
    partial: bool = False,
) -> Product:
    for key, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, key, value)
    await db_session.commit()
    return product


async def delete_product(product: Product, db_session: AsyncSession) -> None:
    await db_session.delete(product)
    await db_session.commit()
