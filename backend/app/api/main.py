from fastapi import APIRouter
from app.api.routes import metrics

api_router = APIRouter()

api_router.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
