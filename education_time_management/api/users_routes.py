from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from education_time_management.users.auth import auth_backend
from education_time_management.users.manager import get_user_manager
from education_time_management.users.models import User
from education_time_management.users.schemas import UserCreate, UserRead

router = APIRouter(prefix="/auth")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    tags=["auth"],
)
