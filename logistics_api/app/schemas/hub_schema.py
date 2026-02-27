from pydantic import BaseModel, Field

class HubBase(BaseModel):
    id: int
    hub_name: str
    city: str

class HubCreate(HubBase):
    pass

class Hub(HubBase):
    id: int
    
    class Config:
        from_attributes = True