"""
Boucle de fond : broadcast KPI + SON en temps réel via WebSocket.
"""
import asyncio
from datetime import datetime, timezone

from app.config import (
    WS_BROADCAST_INTERVAL,
    WS_SON_EVENT_EVERY_N_TICKS,
    OUTAGE_AUTO_RESOLVE_SECONDS,
)
from app.data.cells import CELLS, CELLS_BY_ID
from app.data.kpi import gen_kpi
from app.data import outages as outages_module
from app.son.engine import push_son_event, SON_EVENTS
from app.websocket.manager import manager


async def background_loop() -> None:
    """
    Boucle infinie qui :
      1. Vérifie les pannes à auto-résoudre
      2. Broadcast les KPIs à tous les clients WebSocket
      3. Génère périodiquement un event SON
    """
    tick = 0
    while True:
        tick += 1

        # 1. Auto-résolution des pannes
        to_resolve = outages_module.check_auto_resolve(OUTAGE_AUTO_RESOLVE_SECONDS)
        for cell_id in to_resolve:
            outages_module.resolve_outage(cell_id)
            evt = {
                "ts": datetime.now(timezone.utc).isoformat(),
                "kind": "RECOVERED",
                "cell_id": cell_id,
                "message": f"✅ Self-Healing : service retabli sur {cell_id}",
            }
            SON_EVENTS.append(evt)
            await manager.broadcast({"type": "son", "event": evt})

        # 2. Broadcast des KPIs
        await manager.broadcast({
            "type": "kpi",
            "ts": datetime.now(timezone.utc).isoformat(),
            "cells": [gen_kpi(c) for c in CELLS],
            "outages": list(outages_module.OUTAGES.keys()),
        })

        # 3. Event SON périodique
        if tick % WS_SON_EVENT_EVERY_N_TICKS == 0:
            evt = push_son_event()
            await manager.broadcast({"type": "son", "event": evt})

        await asyncio.sleep(WS_BROADCAST_INTERVAL)