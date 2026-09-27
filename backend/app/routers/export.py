"""
Routes API : export CSV (protegees).
"""
import csv
import io
from datetime import datetime

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.data.cells import CELLS
from app.data.kpi import gen_kpi
from app.dependencies import get_current_tenant_id, require_feature

router = APIRouter(prefix="/api/export", tags=["export"])


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