from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer

try:
    from core.config import settings
except (ImportError, ModuleNotFoundError):
    from lcacollect_config import config

    settings = config.Settings()

azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=settings.AAD_APP_CLIENT_ID,
    tenant_id=settings.AAD_TENANT_ID,
    auto_error=False,
    scopes={
        f"api://{settings.AAD_APP_CLIENT_ID}/user_impersonation": "user_impersonation",
    },
)
