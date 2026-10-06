# Copyright (c) 2026 Jean Thomas Montezuma Montreuil
# All Rights Reserved.
"""
Routes API : export CSV + JSON des KPI (protegees).
"""
import csv
import io
import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.responses import StreamingResponse

from app.data.cells import CELLS
from app.data.kpi import gen_kpi
from app.dependencies import get_current_tenant_id, require_feature

router = APIRouter(prefix="/api/export", tags=["export"])


# ═══════════════════════════════════════════════════════════
# AUTHENTIFICATION PAR API KEY (pour RF Analytics)
# ═══════════════════════════════════════════════════════════

ANALYTICS_API_KEY = os.environ.get("ANALYTICS_API_KEY", "")


def verify_api_key(x_api_key: str = Header(None, alias="X-API-Key")):
    """Vérifie la clé API pour les appels serveur-à-serveur."""
    if not ANALYTICS_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="ANALYTICS_API_KEY non configurée côté serveur"
        )
    if not x_api_key or x_api_key != ANALYTICS_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Clé API invalide ou manquante"
        )
    return True


# ═══════════════════════════════════════════════════════════
# EXPORT CSV (existante, protégée par JWT + feature)
# ═══════════════════════════════════════════════════════════

@router.get("/csv")
def export_csv(
    tenant_id: int = Depends(get_current_tenant_id),
    _ = Depends(require_feature("export_csv")),
):
    """Export CSV des KPIs (feature 'export_csv')."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')

    writer.writerow([
        "Cell ID", "Cluster", "Techno", "Band", "PCI",
        "Latitude", "Longitude", "Azimuth", "Tilt_E", "Tilt_M",
        "Health", "RRC_SR (%)", "Drop_Call (%)",
        "DL_Thpt (Mb/s)", "SINR (dB)", "PRB_Util (%)",
        "HO_SR (%)", "RSRP (dBm)", "Timestamp"
    ])

    for cell in CELLS:
        k = gen_kpi(cell)
        writer.writerow([
            cell["cell_id"], cell["cluster"], cell["techno"], cell["band"], cell["pci"],
            cell["lat"], cell["lon"], cell["azimuth"], cell["tilt_e"], cell["tilt_m"],
            k["health"], k["rrc_sr"], k["dcr"],
            k["dl_throughput"], k["sinr_avg"], k["prb_util"],
            k["ho_sr"], k["rsrp_avg"], k["timestamp"]
        ])

    output.seek(0)
    filename = f"rf_kpi_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


# ═══════════════════════════════════════════════════════════
# EXPORT JSON (nouvelle, pour RF Analytics via API Key)
# ═══════════════════════════════════════════════════════════

@router.get("/kpis")
def export_kpis_json(
    tenant_id: int = 1,
    since: str = None,
    _: bool = Depends(verify_api_key),
):
    """
    Export JSON des KPIs pour RF Analytics.
    
    Authentification : Header 'X-API-Key'
    
    Paramètres :
    - tenant_id : ID du tenant (défaut 1)
    - since : timestamp ISO (optionnel, défaut = 1h avant maintenant)
    
    Retourne :
    {
        "generated_at": "...",
        "tenant_id": 1,
        "kpis": [...],
        "outages": [...]
    }
    """
    # Timestamp de génération
    now = datetime.utcnow()

    # Timestamp de début
    if since:
        try:
            since_dt = datetime.fromisoformat(since.replace("Z", ""))
        except Exception:
            since_dt = now - timedelta(hours=1)
    else:
        since_dt = now - timedelta(hours=1)

    # ─── Construction des KPI ───
    kpis = []
    for cell in CELLS:
        k = gen_kpi(cell)
        kpis.append({
            "site_id": cell.get("site_id", 0),
            "cell_id": cell["cell_id"],
            "timestamp": now.isoformat() + "Z",
            "cluster": cell.get("cluster", "unknown"),
            "techno": cell.get("techno", ""),
            "band": cell.get("band", ""),
            "pci": cell.get("pci", 0),
            "lat": cell.get("lat", 0.0),
            "lon": cell.get("lon", 0.0),
            "rsrp": k.get("rsrp_avg", 0.0),
            "sinr": k.get("sinr_avg", 0.0),
            "dl_throughput": k.get("dl_throughput", 0.0),
            "ul_throughput": k.get("ul_throughput", 0.0),
            "rrc_setup_sr": k.get("rrc_sr", 0.0),
            "drop_call_rate": k.get("dcr", 0.0),
            "prb_util": k.get("prb_util", 0.0),
            "health_score": k.get("health", 0.0),
        })

    # ─── Outages (pannes en cours) ───
    # À implémenter plus tard — on retourne une liste vide pour l'instant
    outages = []

    return {
        "generated_at": now.isoformat() + "Z",
        "since": since_dt.isoformat() + "Z",
        "tenant_id": tenant_id,
        "count": len(kpis),
        "kpis": kpis,
        "outages": outages,
    }