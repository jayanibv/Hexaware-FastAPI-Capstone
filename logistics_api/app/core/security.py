#JWT + BCRYPT
#passlib - password hashing library
#CryptContext - class from passlib to handle password hashing and verification
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#hash password
def hash_password(password: str) -> str:
    safe_password = password.encode("utf-8")[:72]
    return pwd_context.hash(safe_password)

#verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    safe_password = plain_password.encode("utf-8")[:72]
    return pwd_context.verify(safe_password, hashed_password)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

#create access token
def create_access_token(data: dict) -> str:
    to_encode = data.copy() #{"sub": "bhuvi@example.com"}
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire}) #{"sub": "bhuvi@example.com","exp": 2026-02-25T10:30:00Z}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
    return encoded_jwt
