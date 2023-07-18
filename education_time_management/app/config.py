"""Ключевые параметры по умолчанию."""
from dotenv import load_dotenv

import os

load_dotenv()

DB_CONNECTION_URI = os.environ.get("DB_CONNECTION_URI")
BACKEND_URL = os.environ.get("BACKEND_URL")
BACKEND_PORT = os.environ.get("BACKEND_PORT")
BACKEND_URL_WITH_PORT = f"{BACKEND_URL}:{BACKEND_PORT}"
