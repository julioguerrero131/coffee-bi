from fastapi import FastAPI
from app.api.main import api_router
from app.core.config import settings

# uvicorn app.main:app --reload

app = FastAPI(title=settings.PROJECT_NAME)

# Include the API router with a standard prefix
app.include_router(api_router, prefix=settings.API_V1_STR)
