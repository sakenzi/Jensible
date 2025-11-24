from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    id: int
    full_name: str
    email: str
    

class TokenResponse(BaseModel):
    access_token: str
    access_token_expire_time: str
    message: str = "Token generated succesfully"


class MessageResponse(BaseModel):
    status_code: Optional[int] = None
    message: str