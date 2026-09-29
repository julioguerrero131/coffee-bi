from fastapi import APIRouter
from app.api.routes import metrics, sales

api_router = APIRouter()

api_router.include_router(metrics.router, prefix="/metrics", tags=["metrics"])
api_router.include_router(sales.router, prefix="/sales", tags=["sales"])
