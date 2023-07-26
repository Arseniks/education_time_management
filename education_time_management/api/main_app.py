from fastapi import FastAPI

from education_time_management.api.users_routes import router as users_router

app = FastAPI(title="Education time management app")

app.include_router(users_router)
