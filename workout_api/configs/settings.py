from pydantic import Field
from pydantic_settings import BaseSettings


url_db = "postgresql+asyncpg://workout:workout@localhost:5433/workout"

class Settings(BaseSettings):
    DB_URL: str = Field(default=url_db)

settings = Settings()
