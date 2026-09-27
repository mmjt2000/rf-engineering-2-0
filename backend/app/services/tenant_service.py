"""
Service pour la gestion des tenants.
"""
from sqlalchemy.orm import Session
from app.models.tenant import Tenant


def get_tenant_by_slug(db: Session, slug: str) -> Tenant | None:
    return db.query(Tenant).filter(Tenant.slug == slug).first()


def get_tenant_by_id(db: Session, tenant_id: int) -> Tenant | None:
    return db.query(Tenant).filter(Tenant.id == tenant_id).first()


def create_tenant(db: Session, name: str, slug: str, plan: str = "trial") -> Tenant:
    tenant = Tenant(name=name, slug=slug, plan=plan)
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant