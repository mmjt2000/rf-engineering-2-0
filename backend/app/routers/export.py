"""
Routes API : export CSV des KPIs.
"""
import csv
import io
from datetime import datetime

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.data.cells import CELLS
from app.data.kpi import gen_kpi

router = APIRouter(prefix="/api/export", tags=["export"])


@router.get("/csv")
def export_csv():
    """Exporte tous les KPIs dans un fichier CSV téléchargeable."""
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')

    # En-tête
    writer.writerow([
        "Cell ID", "Cluster", "Techno", "Band", "PCI",
        "Latitude", "Longitude", "Azimuth", "Tilt_E", "Tilt_M",
        "Health", "RRC_SR (%)", "Drop_Call (%)",
        "DL_Thpt (Mb/s)", "SINR (dB)", "PRB_Util (%)",
        "HO_SR (%)", "RSRP (dBm)", "Timestamp"
    ])

    # Données : croisement config cellule + KPI généré
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