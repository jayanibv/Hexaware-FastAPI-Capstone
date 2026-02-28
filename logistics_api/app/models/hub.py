from sqlalchemy import Column, String
from app.models.base import BaseModel


class Hub(BaseModel):
    __tablename__ = "hubs"

    hub_name = Column(String, nullable=False)
    city = Column(String, nullable=False)