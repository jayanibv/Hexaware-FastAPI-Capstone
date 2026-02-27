from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Tracking(Base):
    __tablename__ = "tracking_updates"
    
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    status = Column(String)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    shipment_id = Column(Integer, ForeignKey("shipments.id"))