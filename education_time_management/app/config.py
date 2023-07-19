"""Ключевые параметры по умолчанию."""
import os

from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION_URI = os.environ.get("DB_CONNECTION_URI", "postgresql://postgres:postgres@localhost:5432/dev_db")
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost")
BACKEND_PORT = os.environ.get("BACKEND_PORT", "5001")
BACKEND_URL_WITH_PORT = f"{BACKEND_URL}:{BACKEND_PORT}"
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "SECRET")
