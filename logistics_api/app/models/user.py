from  sqlalchemy import Column, Integer, String, Enum
from  sqlalchemy.sql import func
from  app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    customer = "customer"
    agent = "agent"
    admin = "admin"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), nullable=False)