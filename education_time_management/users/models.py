from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from education_time_management.db.db_config import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    registered_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
