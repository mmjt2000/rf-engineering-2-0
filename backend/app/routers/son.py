"""
Routes API : evenements SON (protegees).
"""
from fastapi import APIRouter, Depends

from app.config import SON_EVENTS_API_LIMIT
from app.son.engine import get_recent_events
from app.dependencies import get_current_tenant_id, require_feature

router = APIRouter(prefix="/api/son", tags=["son"])


@router.get("/events")
def son_events(
    tenant_id: int = Depends(get_current_tenant_id),
    _ = Depends(require_feature("son")),
):
    """Derniers evenements SON (feature 'son')."""
    return get_recent_events(SON_EVENTS_API_LIMIT)