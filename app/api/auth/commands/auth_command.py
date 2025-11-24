from sqlalchemy.ext.asyncio import AsyncSession
from app.api.auth.commands.send_email import send_verification_email
from fastapi import HTTPException
import random
from core.redis import redis_client
from app.api.auth.schemas.create import (
    UserCreate,
    UserLogin,
    EmailVerifyCode,
)
from app.api.auth.crud.auth_crud import (
    dal_activate_user,
    dal_create_user_register,
    dal_get_user_by_email,
)
from util.context_utils import (
    create_access_token,
    verify_password,
)
from app.api.auth.schemas.response import (
    TokenResponse,
    MessageResponse,
)
import logging


logger = logging.getLogger(__name__)
CODE_TTL = 300

async def bll_send_verification_email(email: str, code: str):
    await send_verification_email(email, code)

async def bll_register_user(req: UserCreate, db: AsyncSession) -> MessageResponse:
    user_data = req.dict()
    await dal_create_user_register(user_data, db)

    code = f"{random.randint(100000, 999999):06d}"
    redis_key = f"email_verify:{req.email}"

    redis_client.setex(redis_key, CODE_TTL, code)
    logger.info(f"Код {code} сохранён в Redis для {req.email}")

    try:
        await bll_send_verification_email(req.email, code)
    except Exception as e:
        logger.error(f"Ошибка отправки email: {e}")
        raise HTTPException(status_code=500, detail="Не удалось отправить код на почту")
    
    return MessageResponse(message="Код подтверждения отправлен на email")

async def bll_verify_email_code(req: EmailVerifyCode, db: AsyncSession) -> TokenResponse:
    redis_key = f"email_verify:{req.email}"
    stored_code = redis_client.get(redis_key)

    if not stored_code or stored_code != req.code:
        raise HTTPException(status_code=400, detail="Неверный или просроченный код")
    
    redis_client.delete(redis_key)

    user = await dal_activate_user(req.email, db)

    access_token, expire_time = create_access_token({"sub": str(user.id)})

    return TokenResponse(
        access_token=access_token,
        access_token_expire_time=expire_time,
        message="Email успешно подтверждён! Вы вошли в аккаунт"
    )

async def bll_user_login(req: UserLogin, db: AsyncSession) -> TokenResponse:
    user = await dal_get_user_by_email(req.email, db)
    if not user or not verify_password(req.password, user.password):
        raise HTTPException(status_code=401, detail="Неверный email или пароль")
    
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Email не подтверждён. Проверьте почту и введите код.")
    
    access_token, expire_time = create_access_token({"sub": str(user.id)})

    return TokenResponse(
        access_token=access_token,
        access_token_expire_time=expire_time,
        message="Вход выполнен успешно!"
    )