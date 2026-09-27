"""
Génération des KPIs simulés pour chaque cellule.
"""
import random
from datetime import datetime, timezone
from app.data.outages import OUTAGES


def compute_health(rrc: float, dcr: float, thr: float,
                   prb: float, sinr: float) -> float:
    """
    Calcule un score de santé (0-100) à partir des KPIs.
    Pénalise les valeurs hors des seuils normaux.
    """
    score = 100.0
    if rrc < 98:   score -= (98 - rrc) * 5
    if dcr > 1:    score -= (dcr - 1) * 20
    if thr < 30:   score -= (30 - thr) * 1.5
    if prb > 75:   score -= (prb - 75) * 1.0
    if sinr < 12:  score -= (12 - sinr) * 3
    return round(max(0.0, min(100.0, score)), 1)


def gen_kpi(cell: dict) -> dict:
    """Génère un snapshot KPI pour une cellule donnée."""
    # Cas particulier : cellule en panne → KPIs catastrophiques
    if cell["cell_id"] in OUTAGES:
        return {
            "cell_id": cell["cell_id"],
            "rrc_sr": 0.0,
            "dcr": 100.0,
            "dl_throughput": 0.0,
            "prb_util": 0.0,
            "sinr_avg": 0.0,
            "ho_sr": 0.0,
            "rsrp_avg": -120.0,
            "health": 0.0,
            "outage": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

    # Sinon, génération aléatoire réaliste
    rrc  = round(random.uniform(97.2, 99.9), 2)
    dcr  = round(random.uniform(0.15, 1.6), 2)
    thr  = round(random.uniform(12, 68), 1)
    prb  = round(random.uniform(30, 90), 0)
    sinr = round(random.uniform(7, 21), 1)
    ho   = round(random.uniform(96.5, 99.8), 2)
    rsrp = round(random.uniform(-108, -72), 1)

    return {
        "cell_id": cell["cell_id"],
        "rrc_sr": rrc,
        "dcr": dcr,
        "dl_throughput": thr,
        "prb_util": prb,
        "sinr_avg": sinr,
        "ho_sr": ho,
        "rsrp_avg": rsrp,
        "health": compute_health(rrc, dcr, thr, prb, sinr),
        "outage": False,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }