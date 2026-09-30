from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import api_router
from app.core.config import settings

# uvicorn app.main:app --reload

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
      "http://localhost:4200", 
      "http://127.0.0.1:4200",
      "https://coffee-bi.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router with a standard prefix
app.include_router(api_router, prefix=settings.API_V1_STR)
