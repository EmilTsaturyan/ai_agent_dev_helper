import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_key: str
    app_path: str
    model: str

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )


settings = Settings()
BASE_DIR = Path(settings.app_path).resolve()

api_key = settings.api_key
os.environ["GOOGLE_API_KEY"] = api_key