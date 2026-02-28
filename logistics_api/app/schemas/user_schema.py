from pydantic import BaseModel
from uuid import UUID
from app.models.user import UserRole


class UserResponse(BaseModel):
    id: int
    email: str
    role: UserRole

    class Config:
        from_attributes = True