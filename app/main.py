from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import places
from app.common.config import MLSettings

settings = MLSettings()


def create_app():
    app = FastAPI()
    origins = settings.ALLOWED_HOST

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(places.router, tags=["Inference"], prefix="/api")
    return app


app = create_app()
