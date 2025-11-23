from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (
    select,
    update,
)
from models.model import User
from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from util.context_utils import hash_password


async def dal_get_user_by_email(email: str, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()

async def dal_create_user_register(data: dict, db: AsyncSession) -> User:
    user = await dal_get_user_by_email(data["email"], db)
    if user:
        if user.is_active:
            raise HTTPException(status_code=400, detail="Пользователь с таким email уже зарегистрирован")
        else:
            user.full_name = data["full_name"]
            user.password = hash_password(data["password"])
    else:
        user = User(
            full_name = data["full_name"],
            email = data["email"],
            password = hash_password(data["password"]),
            is_active = False
        )            
        db.add(user)
    
    await db.commit()
    await db.refresh(user)
    return user

async def dal_activate_user(email: str, db: AsyncSession) -> User:
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    user.is_active = True
    await db.commit()
    await db.refresh(user)
    return user

