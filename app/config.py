from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "your-secret-key"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()