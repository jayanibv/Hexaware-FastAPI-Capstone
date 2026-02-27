from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Hub(Base):
    __tablename__ = "hubs"
    
    id = Column(Integer, primary_key=True, index=True)
    hub_name = Column(String)
    city = Column(String)
    