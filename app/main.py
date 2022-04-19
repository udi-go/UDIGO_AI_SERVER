from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import places


class App:
    def __init__(self):
        self.app = FastAPI()

    def add_cors_middleware(self):
        origins = [
            "http://localhost",
            "http://localhost:8000",
        ]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
