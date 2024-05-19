from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.schemas.auth as schema
from app.database.config.connect import get_db
from app.services.auth_service import AuthService


router = APIRouter()

@router.post("/token", response_model=schema.Token)
async def token(req_body: schema.CreateToken, session: Session = Depends(get_db)):
    access_token = AuthService(session).create_access_token(req_body)
    return access_token


@router.post("register")
async def register(req_body: schema.Register):
    pass