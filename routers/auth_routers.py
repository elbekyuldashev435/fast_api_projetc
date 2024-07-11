import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from conf.database import session
from conf.models import User as UserModel
from conf.schemas import PasswordSchema
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from fastapi_jwt_auth import AuthJWT


auth_router = APIRouter(prefix="auth")


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@auth_router.post("/signup")
async def signup(user: PasswordSchema, db: Session = Depends(get_db)):

    email_from_db = db.query(UserModel).filter(UserModel.email == user.email).first()
    if email_from_db:
        raise HTTPException(status_code=400, detail="Email already exists!!!")

    username_from_db = db.query(UserModel).filter(UserModel.username == user.username).first()
    if username_from_db:
        raise HTTPException(status_code=400, detail="Username already exists!!!")

    if user.first_name:
        first_name = user.first_name
        if "'" in first_name:
            first_name.replace("'", "%s")

    if user.last_name:
        last_name = user.last_name
        if "'" in last_name:
            last_name.replace("'", "%s")

    new_user = UserModel(
        username=user.username,
        email=user.email,
        first_name=first_name,
        last_name=last_name,
        password=generate_password_hash(user.password),
        is_staff=user.is_staff,
        is_active=user.is_active
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "User created successfully!",
        "user":{
            "username": new_user.username,
            "email": new_user.email,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "is_staff": new_user.is_staff
        }
    }