from pydantic import (
    BaseModel,
    Field,   
    EmailStr,
)
from typing import Optional


class UserCreate(BaseModel):
    full_name: Optional[str] = Field("", max_length=100)
    email: Optional[str] = None
    password: str = Field(..., min_length=8)


class EmailVerifyCode(BaseModel):
    code: str = Field(..., min_length=6, max_length=6)


class UserLogin(BaseModel):
    email: EmailStr = Field(..., max_length=50)
    password: str = Field(..., min_length=8)