import random
from app.config import CLUSTERS, TECHNOS, TECHNOS_WEIGHTS, AZIMUTHS


def gen_cells():
    cells, idx = [], 0
    for cluster in CLUSTERS:
        for _ in range(cluster["n"]):
            idx += 1
            lat = random.uniform(cluster["lat_min"], cluster["lat_max"])
            lon = random.uniform(cluster["lon_min"], cluster["lon_max"])
            techno = random.choices(TECHNOS, weights=TECHNOS_WEIGHTS)[0]
            cells.append({
                "cell_id": f"HTI-{cluster['name'][:3].upper()}-{idx:03d}",
                "cluster": cluster["name"],
                "techno": techno,
                "lat": round(lat, 6),
                "lon": round(lon, 6),
                "pci": random.randint(0, 1007),
                "azimuth": random.choice(AZIMUTHS),
                "tilt_e": random.choice([2, 3, 4, 5, 6]),
                "tilt_m": random.choice([0, 1, 2, 3]),
                "tx_power": random.choice([40, 42, 43, 46]),
                "height_m": random.choice([20, 25, 30, 35, 40]),
                "band": random.choice(["n78", "B3", "B7", "B20", "B1"]),
            })
    return cells


CELLS = gen_cells()
CELLS_BY_ID = {c["cell_id"]: c for c in CELLS}