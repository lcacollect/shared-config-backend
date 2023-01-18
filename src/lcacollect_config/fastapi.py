from fastapi import Depends, Security

from lcacollect_config.connection import get_db
from lcacollect_config.security import azure_scheme


async def get_context(session=Depends(get_db), user=Security(azure_scheme)):
    return {"session": session, "user": user}
