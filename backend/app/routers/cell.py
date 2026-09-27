"""
Routes API : cellules, KPIs, heatmap, drive test, gestion des pannes.
"""
from fastapi import APIRouter

from app.data.cells import CELLS, CELLS_BY_ID
from app.data.kpi import gen_kpi
from app.data.drivetest import DRIVETEST
from app.data.heatmap import get_heatmap
from app.data import outages as outages_module
from app.config import OUTAGE_AUTO_RESOLVE_SECONDS

router = APIRouter(prefix="/api", tags=["cells"])


@router.get("/cells")
def get_cells():
    """Retourne la liste complète des cellules."""
    return {"count": len(CELLS), "cells": CELLS}


@router.get("/kpi/summary")
def kpi_summary():
    """Retourne un snapshot KPI de toutes les cellules."""
    return [gen_kpi(c) for c in CELLS]


@router.get("/kpi/{cell_id}")
def kpi_cell(cell_id: str):
    """Retourne les KPIs d'une cellule spécifique."""
    c = CELLS_BY_ID.get(cell_id)
    if not c:
        return {"error": "cell not found"}
    return gen_kpi(c)


@router.get("/drivetest")
def drivetest():
    """Retourne le parcours drive test simulé."""
    return DRIVETEST


@router.get("/heatmap")
def heatmap():
    """Retourne la grille RSRP interpolée (heatmap)."""
    pts = get_heatmap()
    return {"count": len(pts), "points": pts}


@router.get("/outages")
def get_outages():
    """Liste des cellules actuellement en panne."""
    all_outages = outages_module.get_all_outages()
    return {"outages": all_outages, "count": len(all_outages)}


@router.post("/simulate-outage")
def simulate_outage():
    """Simule la panne d'une cellule aléatoire."""
    import random
    candidates = [c for c in CELLS if not outages_module.is_outage(c["cell_id"])]
    if not candidates:
        return {"error": "Toutes les cellules sont deja en panne"}

    cell = random.choice(candidates)
    ts = outages_module.add_outage(cell["cell_id"])

    evt = {
        "ts": ts,
        "kind": "OUTAGE",
        "cell_id": cell["cell_id"],
        "cluster": cell["cluster"],
        "message": f"⚠️ PANNE detectee sur {cell['cell_id']} ({cell['cluster']}) — Self-Healing active",
    }
    from app.son.engine import SON_EVENTS
    SON_EVENTS.append(evt)
    return {"cell_id": cell["cell_id"], "cluster": cell["cluster"], "event": evt}


@router.post("/resolve-outage/{cell_id}")
def resolve_outage(cell_id: str):
    """Résout manuellement la panne d'une cellule."""
    if outages_module.resolve_outage(cell_id):
        from datetime import datetime, timezone
        evt = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "kind": "RECOVERED",
            "cell_id": cell_id,
            "message": f"✅ Service retabli sur {cell_id}",
        }
        from app.son.engine import SON_EVENTS
        SON_EVENTS.append(evt)
        return {"ok": True, "event": evt}
    return {"ok": False, "error": "Cellule non en panne"}