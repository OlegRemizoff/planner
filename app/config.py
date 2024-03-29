from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_PASS: str
    DB_USER: str
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str

    REDIS_HOST: str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str 

    class Config:
        env_file = ".env"

settings = Settings()


DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

CELERY_BROKER_URL = settings.REDIS_HOST

