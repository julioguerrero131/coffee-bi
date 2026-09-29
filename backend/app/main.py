from fastapi import FastAPI
from app.api.main import api_router

# uvicorn app.main:app --reload

app = FastAPI(title="Coffee BI API")

# Include the API router with a standard prefix
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Hello World"}