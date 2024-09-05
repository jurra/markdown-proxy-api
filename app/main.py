from fastapi import FastAPI
from app.api.endpoints import router as markdown_router

app = FastAPI()

app.include_router(markdown_router, prefix="/api/v1")
