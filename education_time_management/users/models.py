from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from education_time_management.db.db_config import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
