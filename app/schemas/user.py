from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_superadmin: bool
    created_at: datetime

    class Config:
        from_attributes = True

# 👉 Adicione este schema:
class UserLogin(BaseModel):
    username: str
    password: str
