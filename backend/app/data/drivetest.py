"""
Génération du parcours drive test simulé (mesures RSRP/SINR sur un trajet).
"""
import math
import random


def gen_drivetest() -> list[dict]:
    """
    Génère un parcours circulaire simulé autour de Port-au-Prince,
    avec des mesures RSRP/SINR à chaque point.
    """
    base_lat, base_lon = 18.5944, -72.3074
    pts = []
    for i in range(140):
        t = i / 140 * 2 * math.pi
        lat = base_lat + 0.035 * math.cos(t) + random.uniform(-0.002, 0.002)
        lon = base_lon + 0.045 * math.sin(t * 1.4) + random.uniform(-0.002, 0.002)
        pts.append({
            "lat": round(lat, 6),
            "lon": round(lon, 6),
            "rsrp": round(random.uniform(-112, -68), 1),
            "sinr": round(random.uniform(4, 23), 1),
            "t": i,
        })
    return pts


# Parcours global (généré une seule fois au démarrage)
DRIVETEST = gen_drivetest()