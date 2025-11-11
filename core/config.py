from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from core.config_path import BasePath
from typing import Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BasePath}/.env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    