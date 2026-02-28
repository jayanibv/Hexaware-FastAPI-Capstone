from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Tracking(Base):
    __tablename__ = "tracking"

    id = Column(Integer, primary_key=True, index=True)
    tracking_number = Column(String, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, nullable=False)