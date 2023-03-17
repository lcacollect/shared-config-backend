from fastapi import Depends, Security

from lcacollect_config.security import azure_scheme

try:
    from lcacollect_config.connection import get_db

    async def get_context(session=Depends(get_db), user=Security(azure_scheme)):
        return {"session": session, "user": user}

except (ImportError, ModuleNotFoundError):

    async def get_context(user=Security(azure_scheme)):
        return {"user": user}
