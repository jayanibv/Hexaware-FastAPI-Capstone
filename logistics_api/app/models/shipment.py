from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Shipment(Base):
    __tablename__ = "shipments"
    
    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, unique=True)
    source_address = Column(String)
    destination_address = Column(String)
    status = Column(String, default="created")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    customer_id = Column(Integer, ForeignKey("users.id"))

    customer = relationship("User")