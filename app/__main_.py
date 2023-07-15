"""Web-приложение для оптимизации обучения школьников и студентов"""
import argparse
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from app import config


def main():
    description = (
        "Web-application for optimizing the learning of schoolchildren and students\n\n"
        "Dash app at \\ \n" 
        "REST API docs at \\docs\\ "
    )
    formatter = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        prog="education_time_management",
        description=description,
        formatter_class=formatter,
    )
    parser.add_argument(
        "--db_path",
        default=config.DB_PATH,
        type=str,
        help=f"path and file name of QSLite database [default: {config.DB_PATH}]",
    )
    parser.add_argument(
        "--port",
        default=config.BACKEND_PORT,
        type=int,
        help=f"bind socket to this port [default: {config.BACKEND_PORT}]",
    )
    parser.add_argument('--reload')
    args = parser.parse_args()
    config.DB_PATH = Path(args.db_path)
    config.BACKEND_URL_WITH_PORT = f"{config.BACKEND_URL}:{args.port}"

    app = FastAPI()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=args.port,
        log_level="info",
    )


if __name__ == "__main__":
    main()
