from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, Column, create_engine, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from education_time_management.app.config import DB_CONNECTION_URI

DATABASE_URL = DB_CONNECTION_URI

Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session_maker = Session()
