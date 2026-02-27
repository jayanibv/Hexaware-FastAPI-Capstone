from pydantic import BaseModel, Field

class TrackingBase(BaseModel):
    location: str 
    status: str
    updated_at: datetime

class TrackingCreate(TrackingBase):
    pass

class Tracking(TrackingBase):
    id: int
    
    class Config:
        from_attributes = True
