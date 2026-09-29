"""
Routes de gestion des utilisateurs (multi-tenant) avec vérification de quota.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_tenant, get_current_user, PLANS
from app.models.user import User
from app.schemas.user import UserCreateInTenant, UserRead
from app.services.auth_service import hash_password

router = APIRouter(prefix="/api/users", tags=["users"])


def _check_user_quota(tenant, db: Session):
    """Lève 402 si le tenant a atteint son quota d'users."""
    plan = PLANS.get(tenant.plan, PLANS["trial"])
    max_users = plan["max_users"]
    current = db.query(User).filter(User.tenant_id == tenant.id).count()
    if current >= max_users:
        raise HTTPException(
            status_code=402,
            detail=(
                f"Quota d'utilisateurs atteint ({current}/{max_users}) pour le plan "
                f"'{tenant.plan}'. Passez à un plan supérieur pour ajouter des utilisateurs."
            ),
        )


@router.get("", response_model=list[UserRead])
def list_users(
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Liste les utilisateurs du tenant courant."""
    return db.query(User).filter(User.tenant_id == tenant.id).all()


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserCreateInTenant,
    current_user: User = Depends(get_current_user),
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Invite/crée un utilisateur dans le tenant courant (admin seulement)."""
    # Seul un admin peut ajouter des users
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Seuls les administrateurs peuvent ajouter des utilisateurs.",
        )

    # Email unique global
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé")

    _check_user_quota(tenant, db)

    user = User(
        tenant_id=tenant.id,
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password),
        role=payload.role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    tenant=Depends(get_current_tenant),
    db: Session = Depends(get_db),
):
    """Supprime un utilisateur du tenant courant."""
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin requis.")

    if user_id == current_user.id:
        raise HTTPException(
            status_code=400,
            detail="Impossible de se supprimer soi-même.",
        )

    user = db.query(User).filter(
        User.id == user_id,
        User.tenant_id == tenant.id,
    ).first()
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")

    db.delete(user)
    db.commit()
    return None