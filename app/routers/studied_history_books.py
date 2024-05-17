from fastapi import APIRouter
import app.schemas.studied_history_books as schema # type: ignore


router = APIRouter()

@router.get("/studied-history-books", response_model=schema.ListStudiedHistoryBooks)
async def list_studied_history_books():
    pass

@router.get("/studied-history-books/{id}", response_model=schema.ListStudiedHistories)
async def individual_studied_history_book():
    pass