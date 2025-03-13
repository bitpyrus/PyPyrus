from fastapi import APIRouter, HTTPException, Depends
from backend.models import User
from backend.database import SessionLocal

router = APIRouter()

@router.post("/register")
def register_user(username: str, email: str, password: str):
    db = SessionLocal()
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}
