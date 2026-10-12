from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="PDF Q&A Agent"
)

app.include_router(router)