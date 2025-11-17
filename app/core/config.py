# app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My Professional FastAPI App"
    environment: str = "development"
    # Example DB URL if you add SQLAlchemy later:
    database_url: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"     # Load values from a .env file if present
