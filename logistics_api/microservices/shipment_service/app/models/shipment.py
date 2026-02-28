import random
from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, unique=True, nullable=False)
    source_address = Column(String, nullable=False)
    destination_address = Column(String, nullable=False)
    status = Column(String, nullable=False)
    customer_id = Column(Integer, nullable=False)