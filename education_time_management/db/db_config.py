"""Конфигурация и настройка бд"""
from __future__ import annotations

from typing import AsyncGenerator, Optional

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from education_time_management.config import settings


class Base(DeclarativeBase):
    pass


class DbConfig:
    """Класс конфигурации подключения к базе данных"""

    def __init__(self, db_connection_uri: str) -> None:
        self.db_uri: str = db_connection_uri
        self.engine: Optional[AsyncEngine] = None

    def get_engine(self) -> Optional[AsyncEngine]:
        """Получение движка к текущей базе"""
        if self.engine:
            self.engine = create_async_engine(settings.DB_CONNECTION_URI, echo=False)
        return self.engine

    def session_factory(self) -> AsyncSession:
        """Получение сессии подключения к базе"""
        engine = self.get_engine()
        return async_sessionmaker(engine)()

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, AsyncEngine]:
        db = self.session_factory()
        async with db as session:
            yield session


DB_DATA = DbConfig(db_connection_uri=settings.DB_CONNECTION_URI)
