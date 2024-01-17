from fastapi import APIRouter

from api_v1.auth.jwt_auth import router as jwt_router
from api_v1.products.views import router as product_router
from api_v1.reviews.views import router as review_router

router = APIRouter()
router.include_router(router=product_router, prefix="/products", tags=["Products"])
router.include_router(router=review_router, prefix="/reviews", tags=["Reviews"])
router.include_router(router=jwt_router, prefix="/jwt", tags=["JWT"])
