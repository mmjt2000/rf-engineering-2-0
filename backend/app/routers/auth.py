"""
Routes d'authentification : signup, login, me.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.tenant import Tenant
from app.models.user import User
from app.schemas.tenant import TenantCreate
from app.schemas.user import UserCreate, UserRead, Token
from app.services.auth_service import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.services.tenant_service import get_tenant_by_slug, create_tenant

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/signup", response_model=Token, status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, tenant_data: TenantCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau tenant + un utilisateur admin.
    Retourne un JWT immédiatement.
    """
    # Vérifie que le slug tenant et l'email user sont uniques
    if get_tenant_by_slug(db, tenant_data.slug):
        raise HTTPException(status_code=400, detail="Ce slug de tenant existe déjà")

    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail="Cet email est déjà utilisé")

    # Crée le tenant
    tenant = Tenant(
        name=tenant_data.name,
        slug=tenant_data.slug,
        plan="trial",
    )
    db.add(tenant)
    db.flush()  # pour obtenir tenant.id

    # Crée le user admin rattaché
    user = User(
        tenant_id=tenant.id,
        email=payload.email,
        hashed_password=hash_password(payload.password),
        full_name=payload.full_name,
        role="admin",
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Token JWT
    token = create_access_token({
        "sub": str(user.id),
        "tenant_id": user.tenant_id,
        "role": user.role,
    })

    return Token(access_token=token)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Vérifie les credentials et retourne un JWT.
    Utilise le format OAuth2 standard (username + password).
    """
    # Recherche l'utilisateur par email
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Compte désactivé")

    # Met à jour le last_login
    from datetime import datetime, timezone
    user.last_login = datetime.now(timezone.utc)
    db.commit()

    token = create_access_token({
        "sub": str(user.id),
        "tenant_id": user.tenant_id,
        "role": user.role,
    })

    return Token(access_token=token)


@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)):
    """Retourne le profil de l'utilisateur courant."""
    return current_user