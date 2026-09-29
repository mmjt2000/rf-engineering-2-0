"""
Point d'entrée FastAPI pour RF Engineering 2.0.
Assemble les routers, le WebSocket, et sert le frontend statique.
"""
import asyncio
import json
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import SON_EVENTS_INIT_LIMIT
from app.background import background_loop
from app.data.cells import CELLS
from app.data.kpi import gen_kpi
from app.son.engine import SON_EVENTS
from app.websocket.manager import manager
from app.routers import cells as cells_router
from app.routers import sites as sites_router
from app.routers import users as users_router
from app.routers import son as son_router
from app.routers import export as export_router
from app.routers import auth as auth_router
from app.services.auth_service import decode_token


# ============================================================
#  LIFESPAN — démarre/arrête la boucle de fond
# ============================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Démarrage : lance la boucle temps réel
    task = asyncio.create_task(background_loop())
    yield
    # Arrêt propre
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        pass


# ============================================================
#  APPLICATION FASTAPI
# ============================================================
app = FastAPI(
    title="RF Engineering 2.0 API",
    version="2.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================
#  ROUTERS (regroupés par domaine)
# ============================================================
app.include_router(cells_router.router)
app.include_router(sites_router.router)
app.include_router(users_router.router)
app.include_router(son_router.router)
app.include_router
app.include_router(auth_router.router)


# ============================================================
#  WEBSOCKET — broadcast KPI temps réel
# ============================================================
@app.websocket("/ws/kpi")
async def ws_kpi(ws: WebSocket):
    """WebSocket sécurisé par JWT (token passé en query string)."""
    # 1. Récupère le token depuis l'URL : /ws/kpi?token=xxx
    token = ws.query_params.get("token")
    if not token:
        await ws.close(code=1008, reason="Token manquant")
        return

    payload = decode_token(token)
    if not payload:
        await ws.close(code=1008, reason="Token invalide")
        return

    # 2. Valide que l'utilisateur existe et est actif
    user_id = payload.get("sub")
    if not user_id:
        await ws.close(code=1008, reason="Token mal formé")
        return

    # 3. Connexion acceptée
    await manager.connect(ws)

    await ws.send_text(json.dumps({
        "type": "kpi",
        "cells": [gen_kpi(c) for c in CELLS],
    }))
    await ws.send_text(json.dumps({
        "type": "son_init",
        "events": SON_EVENTS[-SON_EVENTS_INIT_LIMIT:],
    }))

    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(ws)
    except Exception:
        manager.disconnect(ws)

# ============================================================
#  FRONTEND STATIQUE
# ============================================================
FRONTEND_DIR = Path(__file__).parent.parent.parent / "frontend"

if FRONTEND_DIR.exists():
    @app.get("/")
    def index():
        return FileResponse(FRONTEND_DIR / "index.html", media_type="text/html; charset=utf-8")

    @app.get("/login.html")
    def login_page():
        return FileResponse(FRONTEND_DIR / "login.html", media_type="text/html; charset=utf-8")

    @app.get("/signup.html")
    def signup_page():
        # Sera créé plus tard
        return FileResponse(FRONTEND_DIR / "signup.html", media_type="text/html; charset=utf-8") if (FRONTEND_DIR / "signup.html").exists() else FileResponse(FRONTEND_DIR / "login.html", media_type="text/html; charset=utf-8")
    
    @app.get("/billing.html")
    def billing_page():
        return FileResponse(FRONTEND_DIR / "billing.html", media_type="text/html; charset=utf-8")
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/sites.html")
    def sites_page():
        return FileResponse(FRONTEND_DIR / "sites.html", media_type="text/html; charset=utf-8")