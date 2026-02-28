from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def register(self, db: Session, data):
        existing_user = db.query(User).filter(
            User.email == data.email
        ).first()

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            email=data.email,
            password_hash=hash_password(data.password),
            role=data.role.upper()
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {"message": "User registered successfully"}

    def login(self, db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({
            "sub": str(user.id),
            "role": user.role
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }