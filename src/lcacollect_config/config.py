from typing import Any

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_STR: str = "/api"
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://0.0.0.0:3000",
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Azure AD
    AAD_OPENAPI_CLIENT_ID: str
    AAD_APP_CLIENT_ID: str
    AAD_TENANT_ID: str
    AAD_TEST_CLIENT_SECRET: str | None

    # Postgres
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    POSTGRES_SSL: bool = False
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    ROUTER_URL: AnyHttpUrl

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: str | None, values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
            port=values.get("POSTGRES_PORT"),
        )

    class Config:
        case_sensitive = True
