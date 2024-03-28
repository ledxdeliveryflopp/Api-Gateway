from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class JwtSettings(BaseSettings):

    jwt_secret: str
    jwt_algorithm: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class SqlSettings(BaseSettings):
    """Настройки для БД"""
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def db_full_url(self) -> str:
        return (f"postgresql+asyncpg://{self.sql_user}:{self.sql_password}@"
                f"{self.sql_host}:{self.sql_port}/{self.sql_name}")


class Settings(BaseSettings):
    """Все настройки"""
    jwt_settings: JwtSettings
    sql_settings: SqlSettings


@lru_cache()
def init_settings():
    """Инициализация настроек"""
    all_settings = Settings(jwt_settings=JwtSettings(), sql_settings=SqlSettings())
    return all_settings


settings = init_settings()

