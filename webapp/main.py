from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from conf.config import settings
from users.views import router as users_router

app = FastAPI()


def setup_middleware(app: FastAPI) -> None:
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
            allow_headers=["Content-Type", "Authorization", "Set-Cookie", "Access-Control-Allow-Origin",
                           "Access-Control-Allow-Headers"],
        )


def setup_routers(app: FastAPI) -> None:
    app.include_router(users_router)


setup_routers(app)
setup_middleware(app)
