"""Web-приложение для оптимизации обучения школьников и студентов"""
import argparse

import uvicorn
from fastapi import FastAPI

from education_time_management.app.config import settings


def main() -> None:
    description = (
        "Web-приложение для оптимизации обучения школьников и студентов\n\n" "RESTapi документация по пути \\docs\\ "
    )
    formatter = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        prog="education_time_management",
        description=description,
        formatter_class=formatter,
    )
    parser.add_argument(
        "--db_connection_uri",
        default=settings.DB_CONNECTION_URI,
        type=str,
        help=f"полный URI для бд PostgreSQL [по умолчанию: {settings.DB_CONNECTION_URI}]",
    )
    parser.add_argument(
        "--port",
        default=settings.BACKEND_PORT,
        type=int,
        help=f"привязать сокет к этому порту [по умолчанию: {settings.BACKEND_PORT}]",
    )
    parser.add_argument("--reload")
    args = parser.parse_args()
    settings.DB_CONNECTION_URI = args.db_connection_uri
    settings.BACKEND_URL_WITH_PORT = f"{settings.BACKEND_URL}:{args.port}"

    app = FastAPI()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=args.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
