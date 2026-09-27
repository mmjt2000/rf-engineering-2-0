"""
Dependances FastAPI : utilisateur, tenant, features.
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tenant import Tenant
from app.models.user import User
from app.services.auth_service import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


# ============================================================
#  PLANS ET FEATURES
# ============================================================
PLANS = {
    "trial": {
        "max_sites": 3,
        "max_users": 2,
        "features": ["kpis_basic", "map"],
    },
    "starter": {
        "max_sites": 10,
        "max_users": 5,
        "features": ["kpis_basic", "map", "son", "export_csv"],
    },
    "pro": {
        "max_sites": 50,
        "max_users": 20,
        "features": ["kpis_basic", "map", "son", "export_csv", "heatmap", "self_healing"],
    },
    "enterprise": {
        "max_sites": 9999,
        "max_users": 9999,
        "features": ["all"],
    },
}


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Recupere l'utilisateur courant depuis le JWT."""
    payload = decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide ou expire",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token mal forme")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Utilisateur inactif ou inexistant")

    return user


def get_current_tenant_id(user: User = Depends(get_current_user)) -> int:
    """Retourne le tenant_id de l'utilisateur courant."""
    return user.tenant_id


def get_current_tenant(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Tenant:
    """Retourne le tenant de l'utilisateur courant."""
    tenant = db.query(Tenant).filter(Tenant.id == user.tenant_id).first()
    if not tenant or not tenant.is_active:
        raise HTTPException(status_code=403, detail="Tenant inactif ou inexistant")
    return tenant


def require_feature(feature: str):
    """
    Genere une dependance qui verifie que le plan du tenant inclut la feature.
    Usage : Depends(require_feature("son"))
    """
    def checker(tenant: Tenant = Depends(get_current_tenant)):
        plan = PLANS.get(tenant.plan, PLANS["trial"])
        features = plan.get("features", [])
        if feature not in features and "all" not in features:
            raise HTTPException(
                status_code=402,
                detail=f"Feature '{feature}' non incluse dans le plan '{tenant.plan}'",
            )
        return tenant
    return checker