from fastapi import APIRouter
import app.schemas.auth as schema # type: ignore


router = APIRouter()

@router.post("/token", response_model=schema.Token)
async def token(req_body: schema.CreateToken):
    pass


@router.post("register")
async def register(req_body: schema.Register):
    pass