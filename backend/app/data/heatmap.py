"""
Génération de la heatmap RSRP par interpolation IDW.
(Inverse Distance Weighting — plus proche = plus d'influence)
"""
import math
from app.config import CLUSTERS
from app.data.cells import CELLS


def compute_rsrp_at(lat: float, lon: float, k: int = 4) -> float:
    """
    Interpole le RSRP en (lat, lon) à partir des k cellules les plus proches.
    Retourne une valeur en dBm (plus négatif = plus mauvais signal).
    """
    dists = []
    for c in CELLS:
        d = math.hypot(c["lat"] - lat, c["lon"] - lon)
        if d < 1e-9:
            return -75.0  # pile sur une cellule
        dists.append((d, c))
    dists.sort(key=lambda x: x[0])
    nearest = dists[:k]

    num, den = 0.0, 0.0
    for d, c in nearest:
        w = 1.0 / (d ** 2)
        # RSRP "réaliste" simulé par cellule : entre -115 et -75 dBm
        # Utilise un hash stable du cell_id pour garantir la cohérence
        rsrp_cell = -115 + (hash(c["cell_id"]) % 40)
        num += w * rsrp_cell
        den += w
    return num / den if den > 0 else -100.0


def gen_heatmap() -> list[dict]:
    """
    Génère une grille de points RSRP interpolés,
    limitée aux zones proches des villes (pour éviter les calculs inutiles en mer).
    """
    points = []
    step = 0.02  # pas de la grille en degrés (~2 km)
    seen = set()  # évite les doublons entre clusters

    for cluster in CLUSTERS:
        # Centre du cluster (milieu de sa bbox)
        c_lat = (cluster["lat_min"] + cluster["lat_max"]) / 2
        c_lon = (cluster["lon_min"] + cluster["lon_max"]) / 2
        # Rayon de la zone couverte (en degrés)
        r_lat = 0.30
        r_lon = 0.30

        lat = c_lat - r_lat
        while lat <= c_lat + r_lat:
            lon = c_lon - r_lon
            while lon <= c_lon + r_lon:
                # Ne garder que les points à moins de ~35 km d'une cellule
                d_min = min(
                    math.hypot(c["lat"] - lat, c["lon"] - lon)
                    for c in CELLS
                )
                if d_min < 0.35:
                    key = (round(lat, 3), round(lon, 3))
                    if key not in seen:
                        seen.add(key)
                        rsrp = compute_rsrp_at(lat, lon)
                        points.append({
                            "lat": round(lat, 4),
                            "lon": round(lon, 4),
                            "rsrp": round(rsrp, 1),
                        })
                lon += step
            lat += step
    return points


# Cache global : généré une seule fois au démarrage
_HEATMAP_CACHE: list[dict] | None = None


def get_heatmap() -> list[dict]:
    """Retourne la heatmap (avec cache)."""
    global _HEATMAP_CACHE
    if _HEATMAP_CACHE is None:
        _HEATMAP_CACHE = gen_heatmap()
    return _HEATMAP_CACHE