"""
Schemas Pydantic pour les tenants.
"""
from datetime import datetime
from pydantic import BaseModel, Field


class TenantBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    slug: str = Field(..., min_length=2, max_length=60)


class TenantCreate(TenantBase):
    plan: str = "trial"


class TenantRead(TenantBase):
    id: int
    plan: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True