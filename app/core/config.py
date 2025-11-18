from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Professional CQRS + Mediator API"
    environment: str = "development"

    class Config:
        env_file = ".env"
