"""
Schemas Pydantic pour les sites.
"""
from pydantic import BaseModel, Field


class SiteBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    lat: float = Field(..., ge=-90, le=90)
    lon: float = Field(..., ge=-180, le=180)
    cluster: str | None = Field(None, max_length=80)


class SiteCreate(SiteBase):
    pass


class SiteUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=120)
    lat: float | None = Field(None, ge=-90, le=90)
    lon: float | None = Field(None, ge=-180, le=180)
    cluster: str | None = Field(None, max_length=80)


class SiteRead(SiteBase):
    id: int
    tenant_id: int

    class Config:
        from_attributes = True