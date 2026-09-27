"""
Configuration et constantes globales pour RF Engineering 2.0.
"""

# ============================================================
#  GÉOGRAPHIE — zones de sécurité (terre ferme garantie)
# ============================================================
CLUSTERS = [
    {
        "name": "Port-au-Prince", "n": 28,
        "lat_min": 18.50, "lat_max": 18.62,
        "lon_min": -72.30, "lon_max": -72.15,
    },
    {
        "name": "Cap-Haïtien", "n": 12,
        "lat_min": 19.60, "lat_max": 19.72,
        "lon_min": -72.25, "lon_max": -72.05,
    },
    {
        "name": "Jacmel", "n": 8,
        "lat_min": 18.25, "lat_max": 18.35,
        "lon_min": -72.55, "lon_max": -72.35,
    },
    {
        "name": "Les Cayes", "n": 6,
        "lat_min": 18.25, "lat_max": 18.35,
        "lon_min": -73.80, "lon_max": -73.60,
    },
]

# Technologies mobiles supportées
TECHNOS = ["5G-NR", "LTE", "UMTS", "GSM"]

# Pondération des technologies (5G et LTE plus fréquentes)
TECHNOS_WEIGHTS = [4, 6, 1, 1]

# Azimuths standards (en degrés)
AZIMUTHS = [0, 60, 120, 180, 240, 300]

# ============================================================
#  WEBSOCKET — paramètres de broadcast
# ============================================================
WS_BROADCAST_INTERVAL = 2  # Intervalle de broadcast KPI (secondes)
WS_SON_EVENT_EVERY_N_TICKS = 3  # Un event SON tous les 3 ticks

# ============================================================
#  GESTION DES PANNES (OUTAGES)
# ============================================================
OUTAGE_AUTO_RESOLVE_SECONDS = 10  # Auto-résolution après X secondes
SON_EVENTS_MAX = 150  # Taille max du buffer SON events

# ============================================================
#  LIMITES API
# ============================================================
SON_EVENTS_INIT_LIMIT = 15  # Events envoyés au démarrage du WS
SON_EVENTS_API_LIMIT = 40  # Events retournés par /api/son/events

# ============================================================
#  CHEMINS
# ============================================================
from pathlib import Path
FRONTEND_DIR = Path(__file__).parent.parent.parent / "frontend"