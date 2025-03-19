import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Конфигурация приложения"""
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    CACHE_TYPE: str = "simple"
    CACHE_DEFAULT_TIMEOUT: int = 300
