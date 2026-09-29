"""
Routes CRUD des sites (multi-tenant) avec vérification de quota.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_tenant, PLANS
from app.models.site import Site
from app.schemas.site import SiteCreate, SiteRead, SiteUpdate

router = APIRouter(prefix="/api/sites", tags=["sites"])


def _check_site_quota(tenant, db: Session):
    """Lève 402 si le tenant a atteint son quota de sites."""
    plan = PLANS.get(tenant.plan, PLANS["trial"])
    max_sites = plan["max_sites"]
    current = db.query(Site).filter(Site.tenant_id == tenant.id).count()
    if current >= max_sites:
        raise HTTPException(
            status_code=402,
            detail=(
                f"Quota de sites atteint ({current}/{max_sites}) pour le plan "
                f"'{tenant.plan}'. Passez à un plan supérieur pour ajouter des sites."
            ),
        )


@router.get("", response_model=list[SiteRead])
def list_sites(
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Liste les sites du tenant courant."""
    return db.query(Site).filter(Site.tenant_id == tenant.id).all()


@router.post("", response_model=SiteRead, status_code=status.HTTP_201_CREATED)
def create_site(
    payload: SiteCreate,
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Crée un nouveau site pour le tenant courant (quota vérifié)."""
    _check_site_quota(tenant, db)

    site = Site(
        tenant_id=tenant.id,
        name=payload.name,
        lat=payload.lat,
        lon=payload.lon,
        cluster=payload.cluster,
    )
    db.add(site)
    db.commit()
    db.refresh(site)
    return site


@router.get("/{site_id}", response_model=SiteRead)
def get_site(
    site_id: int,
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Récupère un site (vérifie qu'il appartient au tenant)."""
    site = db.query(Site).filter(
        Site.id == site_id,
        Site.tenant_id == tenant.id,
    ).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site non trouvé")
    return site


@router.patch("/{site_id}", response_model=SiteRead)
def update_site(
    site_id: int,
    payload: SiteUpdate,
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Modifie un site du tenant courant."""
    site = db.query(Site).filter(
        Site.id == site_id,
        Site.tenant_id == tenant.id,
    ).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site non trouvé")

    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(site, k, v)
    db.commit()
    db.refresh(site)
    return site


@router.delete("/{site_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_site(
    site_id: int,
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Supprime un site du tenant courant."""
    site = db.query(Site).filter(
        Site.id == site_id,
        Site.tenant_id == tenant.id,
    ).first()
    if not site:
        raise HTTPException(status_code=404, detail="Site non trouvé")
    db.delete(site)
    db.commit()
    return None