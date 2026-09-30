from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://inventory:inventory@db:5432/inventory"
    secret_key: str = "change"
    admin_email: str = "admin@estoque.local"
    admin_password: str = "Admin123!"
    admin_name: str = "Administrador"

    model_config = SettingsConfigDict(extra="ignore")

    @field_validator("database_url", mode="before")
    @classmethod
    def use_psycopg3_driver(cls, value: str) -> str:
        """Converte a URL do Render para o driver psycopg 3 instalado."""
        if isinstance(value, str):
            if value.startswith("postgres://"):
                return value.replace("postgres://", "postgresql+psycopg://", 1)
            if value.startswith("postgresql://"):
                return value.replace("postgresql://", "postgresql+psycopg://", 1)
        return value


settings = Settings()
