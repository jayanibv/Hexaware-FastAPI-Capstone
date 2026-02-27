from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr = Field(..., description="User email address")
    role: str

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=50)

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True