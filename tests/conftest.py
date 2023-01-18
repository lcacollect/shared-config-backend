import os

import pytest


@pytest.fixture()
def settings_env():
    envs = {
        "SERVER_NAME": "LCA Test",
        "SERVER_HOST": "http://test",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_USER": "postgresuser",
        "POSTGRES_PASSWORD": "mypassword",
        "POSTGRES_DB": "lca-assembly",
        "POSTGRES_PORT": "5632",
        "AAD_OPENAPI_CLIENT_ID": "b7fc0d3e-fdd9-4260-8b01-12cad623c64a",
        "AAD_APP_CLIENT_ID": "40c35f10-9d17-43dc-bf6c-6208945c98c6",
        "AAD_TENANT_ID": "11be1538-79d8-4939-82b8-b767805d825b",
        "AAD_TEST_CLIENT_SECRET": "RmQ7Q~ejj0xaB566qjekYB6Oivq06Sk4Q69Hw",
    }
    for key, value in envs.items():
        os.environ[key] = value

    yield envs
