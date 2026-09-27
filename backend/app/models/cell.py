from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base, TimestampMixin


class Cell(Base, TimestampMixin):
    __tablename__ = "cells"

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey("sites.id"), nullable=False, index=True)
    cell_id = Column(String(60), nullable=False, index=True)
    techno = Column(String(20), nullable=True)
    pci = Column(Integer, nullable=True)
    azimuth = Column(Integer, nullable=True)
    tilt_e = Column(Integer, nullable=True)
    tilt_m = Column(Integer, nullable=True)
    tx_power = Column(Integer, nullable=True)
    height_m = Column(Integer, nullable=True)
    band = Column(String(20), nullable=True)

    site = relationship("Site", back_populates="cells")

    def __repr__(self):
        return f"<Cell {self.cell_id}>"