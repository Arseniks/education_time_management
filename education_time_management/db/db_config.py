from __future__ import annotations

from typing import Optional

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker

from education_time_management.app.config import settings


class DbConfig:
    """Класс конфигурации подключения к базе данных"""

    _self = None

    def __new__(cls, *args, **kwargs) -> DbConfig:
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def __init__(self, db_connection_uri: str) -> None:
        self.db_uri = db_connection_uri
        self.engine = None

    def get_engine(self) -> Optional[Engine]:
        """Получаю engine к текущей базе"""
        if self.engine:
            self.engine = create_engine(settings.DB_CONNECTION_URI, echo=False)
        return self.engine

    def session_factory(self) -> Session:
        """Создание сессии"""
        engine = create_engine(self.db_uri)
        session = sessionmaker(bind=engine)
        return session()


DB_DATA = DbConfig(db_connection_uri=settings.DB_CONNECTION_URI)
