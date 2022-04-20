from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import places


def create_app():
    app = FastAPI()

    def add_cors_middleware():
        origins = [
            "http://localhost",
            "http://localhost:8000",
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        app.add_cors_middleware()

    return app
    

app = create_app()