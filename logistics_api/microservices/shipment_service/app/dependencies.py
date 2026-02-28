from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8001/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = decode_token(token)
    return user_id


def require_role(allowed_roles: list):
    def role_checker(token: str = Depends(oauth2_scheme)):
        from jose import jwt
        from app.core.config import settings

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        role = payload.get("role")

        if role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")

        return payload.get("sub")

    return role_checker