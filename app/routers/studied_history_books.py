from fastapi import APIRouter, Depends
import app.schemas.studied_history_books as schema
from app.utils.auth import oauth2_scheme


router = APIRouter()

@router.get("/studied-history-books", response_model=schema.ListStudiedHistoryBooks)
async def list_studied_history_books(access_token: str = Depends(oauth2_scheme)):
    pass

@router.get("/studied-history-books/{id}", response_model=schema.ListStudiedHistories)
async def individual_studied_history_book(access_token: str = Depends(oauth2_scheme)):
    pass