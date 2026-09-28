from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Notizen-API"

    model_config = SettingsConfigDict(env_file=".env")
