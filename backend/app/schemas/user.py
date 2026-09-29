"""
Schemas Pydantic pour les utilisateurs.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    role: str = "user"


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserCreateInTenant(BaseModel):
    """Pour inviter un user dans le tenant courant (admin seulement)."""
    email: EmailStr
    full_name: str | None = None
    password: str = Field(..., min_length=8)
    role: str = "user"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRead(UserBase):
    id: int
    tenant_id: int
    is_active: bool
    created_at: datetime
    plan: Optional[str] = None
    tenant_name: Optional[str] = None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"