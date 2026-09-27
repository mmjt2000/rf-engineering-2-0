"""
Routes API : événements SON (Self-Organizing Network).
"""
from fastapi import APIRouter

from app.config import SON_EVENTS_API_LIMIT
from app.son.engine import get_recent_events

router = APIRouter(prefix="/api/son", tags=["son"])


@router.get("/events")
def son_events():
    """Retourne les derniers événements SON (les plus récents en premier)."""
    return get_recent_events(SON_EVENTS_API_LIMIT)