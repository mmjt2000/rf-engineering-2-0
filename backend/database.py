"""
Configuration de la base de données SQLAlchemy.
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Charge les variables depuis .env
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL manquant dans .env")

# Moteur SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Passe à True pour voir les requêtes SQL
    pool_pre_ping=True,  # Vérifie la connexion avant chaque usage
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base pour les modèles
Base = declarative_base()


def get_db():
    """Dépendance FastAPI pour obtenir une session DB."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()