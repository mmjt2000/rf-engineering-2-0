"""
Point d'entrée pour Uvicorn.
Lance l'application FastAPI définie dans app.main.

Usage local :
    uvicorn main:app --reload --port 8000

Usage production (Dockerfile) :
    uvicorn main:app --host 0.0.0.0 --port 8000
"""
from app.main import app

__all__ = ["app"]