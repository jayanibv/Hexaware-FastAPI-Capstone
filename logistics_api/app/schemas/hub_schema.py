from pydantic import BaseModel
from datetime import datetime

class HubCreate(BaseModel):
    name: str
    location: str

class HubResponse(BaseModel):
    id: int
    name: str
    location: str
    created_at: datetime

    model_config = {"from_attributes": True}