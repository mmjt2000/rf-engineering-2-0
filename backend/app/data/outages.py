"""
Gestion de l'état des pannes réseau (outages).
Un outage = une cellule qui tombe en panne (simulée ou réelle).
"""
from datetime import datetime, timezone


# État global : {cell_id: timestamp_of_outage}
# Modifié par les routes /api/simulate-outage et /api/resolve-outage
OUTAGES: dict[str, str] = {}


def add_outage(cell_id: str) -> str:
    """Marque une cellule comme en panne. Retourne le timestamp ISO."""
    ts = datetime.now(timezone.utc).isoformat()
    OUTAGES[cell_id] = ts
    return ts


def resolve_outage(cell_id: str) -> bool:
    """Résout une panne. Retourne True si elle existait."""
    if cell_id in OUTAGES:
        del OUTAGES[cell_id]
        return True
    return False


def is_outage(cell_id: str) -> bool:
    """Vérifie si une cellule est actuellement en panne."""
    return cell_id in OUTAGES


def get_all_outages() -> list[str]:
    """Retourne la liste des cellules en panne."""
    return list(OUTAGES.keys())


def check_auto_resolve(threshold_seconds: int) -> list[str]:
    """
    Vérifie quelles pannes dépassent le seuil d'auto-résolution.
    Retourne la liste des cell_ids à résoudre.
    """
    now = datetime.now(timezone.utc)
    to_resolve = []
    for cell_id, ts_str in list(OUTAGES.items()):
        ts = datetime.fromisoformat(ts_str)
        if (now - ts).total_seconds() > threshold_seconds:
            to_resolve.append(cell_id)
    return to_resolve