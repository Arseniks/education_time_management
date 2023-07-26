from typing import AsyncGenerator, Type

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from education_time_management.db.db_config import DB_DATA
from education_time_management.users.models import User


async def get_user_db(async_session: AsyncSession = Depends(DB_DATA.get_async_session)):
    yield SQLAlchemyUserDatabase(async_session, User)
