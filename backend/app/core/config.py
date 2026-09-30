from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    PROJECT_NAME: str = "Coffee BI API"
    API_V1_STR: str = "/api/v1"
    
    # Database
    MONGO_URI: str
    MONGO_DB: str
    MONGO_COLLECTION_SALES: str
    
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

settings = Settings()
