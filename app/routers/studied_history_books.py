from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.studied_history_books import ListStudiedHistoryBooks, ListStudiedHistories
from app.database.config.connect import get_db
from app.services.studied_history_book_service import StudiedHistoryBookService
from app.database.model.models import User


router = APIRouter()

@router.get("/studied-history-books", response_model=ListStudiedHistoryBooks)
async def list_studied_history_books(session: Session = Depends(get_db)):
    user = User(id=1, name="Tanaka",email="Tanaka@example.com",password="password")
    studied_history_books = StudiedHistoryBookService(session, user).list_studied_history_books()

    return studied_history_books

@router.get("/studied-history-books/{book_id}")
async def individual_studied_history_book(book_id: int, session: Session = Depends(get_db)):
    user = User(id=1, name="Tanaka",email="Tanaka@example.com",password="password")
    studied_histories = StudiedHistoryBookService(session, user).individual_studied_history_book(book_id)

    return studied_histories