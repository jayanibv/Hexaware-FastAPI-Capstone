from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import relationship

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, unique=True, index=True)
    source_address = Column(String, nullable=False)
    destination_address = Column(String, nullable=False)
    status = Column(String, default="created")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    customer_id = Column(Integer, ForeignKey("users.id"))
    hub_id = Column(Integer, ForeignKey("hubs.id"), nullable=True)