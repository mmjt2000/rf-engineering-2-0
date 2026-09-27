from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base, TimestampMixin


class Site(Base, TimestampMixin):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False, index=True)
    name = Column(String(120), nullable=False)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    cluster = Column(String(80), nullable=True)

    tenant = relationship("Tenant", back_populates="sites")
    cells = relationship("Cell", back_populates="site", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Site {self.name}>"