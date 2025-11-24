from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    Depends,
    APIRouter,
)
from database.db import get_db
from app.api.auth.schemas.create import (
    UserCreate,
    UserLogin,
    EmailVerifyCode,
)
from app.api.auth.commands.auth_command import (
    bll_send_verification_email,
    bll_user_login,
    bll_verify_email_code,
    bll_register_user
)
from app.api.auth.schemas.response import (
    TokenResponse,
    MessageResponse,
)


router = APIRouter()

@router.post("/register", response_model=MessageResponse, summary="Регистрация пользователя")
async def user_register(req: UserCreate, db: AsyncSession = Depends(get_db)):
    return await bll_register_user(req, db)

@router.post("/verify_email", response_model=TokenResponse, summary="Верификация почты")
async def verify_email(req: EmailVerifyCode, db: AsyncSession = Depends(get_db)):
    return await bll_verify_email_code(req, db)

@router.post("/login", response_model=TokenResponse, summary="Логин")
async def user_login(req: UserLogin, db: AsyncSession = Depends(get_db)):
    return await bll_user_login(req, db)