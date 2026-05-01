from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middlewares.exceptions_handlers import catch_exception_middleware

app = FastAPI(title="Medical Assistance API", description="API for AI medical assistance chatbot", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=["*"],
)

app.middleware("http")(catch_exception_middleware)