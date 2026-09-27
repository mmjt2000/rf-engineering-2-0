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
from app.routers import son as son_router
from app.routers import export as export_router
from app.routers import auth as auth_router


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
app.include_router(son_router.router)
app.include_router
app.include_router(auth_router.router)


# ============================================================
#  WEBSOCKET — broadcast KPI temps réel
# ============================================================
@app.websocket("/ws/kpi")
async def ws_kpi(ws: WebSocket):
    """WebSocket pour recevoir les KPIs et events SON en temps réel."""
    await manager.connect(ws)

    # Envoi initial : snapshot KPI + derniers events SON
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
            # On attend un ping du client (garde la connexion ouverte)
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
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

    @app.get("/")
    def index():
        return FileResponse(FRONTEND_DIR / "index.html")