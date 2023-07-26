"""Web-приложение для оптимизации обучения школьников и студентов"""
import typer
import uvicorn

from education_time_management.config import settings


def main(
    db_connection_uri: str = settings.DB_CONNECTION_URI,
    port: int = settings.BACKEND_PORT,
    reload: bool = True,
) -> None:
    """
    Web-приложение для оптимизации обучения школьников и студентов

    RESTapi документация по пути \\docs\\
    """
    settings.DB_CONNECTION_URI = db_connection_uri
    settings.BACKEND_URL_WITH_PORT = f"{settings.BACKEND_URL}:{port}"

    uvicorn.run("education_time_management.api.main_app:app", host="0.0.0.0", port=port, log_level="info", reload=reload)


if __name__ == "__main__":
    typer.run(main)
