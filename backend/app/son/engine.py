"""
Moteur SON (Self-Organizing Network) — simulation des événements d'optimisation automatique.
"""
import random
from datetime import datetime, timezone

from app.config import SON_EVENTS_MAX
from app.data.cells import CELLS


# Templates d'événements SON par type
SON_TEMPLATES = [
    ("MRO",          "Ajustement A3 offset sur {cell} ({val} dB)"),
    ("MLB",          "Rééquilibrage de charge : {cell} → voisin (PRB {val}%)"),
    ("CCO",          "Correction tilt électrique sur {cell} ({val}°)"),
    ("ANR",          "Nouvelle relation X2 ajoutée sur {cell}"),
    ("ICIC",         "Activation ICIC sur {cell} (SINR +{val} dB)"),
    ("Self-Healing", "Compensation outage détectée sur {cell}"),
    ("PCI",          "Résolution conflit PCI sur {cell} ({val})"),
]

# Buffer global des événements SON (limité à SON_EVENTS_MAX)
SON_EVENTS: list[dict] = []


def _trim_events() -> None:
    """Garde seulement les SON_EVENTS_MAX derniers événements."""
    while len(SON_EVENTS) > SON_EVENTS_MAX:
        SON_EVENTS.pop(0)


def push_son_event() -> dict:
    """Génère un événement SON aléatoire et l'ajoute au buffer."""
    cell = random.choice(CELLS)
    kind, tpl = random.choice(SON_TEMPLATES)
    val = round(random.uniform(0.5, 15), 1)
    evt = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "kind": kind,
        "cell_id": cell["cell_id"],
        "cluster": cell["cluster"],
        "message": tpl.format(cell=cell["cell_id"], val=val),
    }
    SON_EVENTS.append(evt)
    _trim_events()
    return evt


def push_custom_event(kind: str, cell: dict, message: str) -> dict:
    """Ajoute un événement SON personnalisé (ex: OUTAGE, RECOVERED)."""
    evt = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "kind": kind,
        "cell_id": cell["cell_id"],
        "cluster": cell.get("cluster", ""),
        "message": message,
    }
    SON_EVENTS.append(evt)
    _trim_events()
    return evt


def get_recent_events(limit: int) -> list[dict]:
    """Retourne les derniers événements (les plus récents)."""
    return SON_EVENTS[-limit:]