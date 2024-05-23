from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.repositories.book_repository import BookRepository
from app.repositories.studying_book_repository import StudyingBookRepository
from app.schemas.studied_history_books import ListStudiedHistoryBooks, StudiedHistoryBook
from app.database.model.models import User

class StudiedHistoryBookService:
    def __init__(self, session: Session, user: User):
        self.studying_book_repository = StudyingBookRepository(session)
        self.book_repository = BookRepository(session)
        self.user = user
        self.session = session

    
    def list_studied_history_books(self) -> ListStudiedHistoryBooks:
        studied_history_books = self.book_repository.user_has_complated_in_count_list(self.user.id)

        response_studied_history_book = []
        for studied_history_book in studied_history_books:
            response_studied_history_book.append(
                StudiedHistoryBook(
                    book_id=studied_history_book.id,
                    title=studied_history_book.title,
                    img_url=studied_history_book.img_url,
                    studied_count=studied_history_book.studied_count
                )
            )
        
        return ListStudiedHistoryBooks(
            studied_history_books=response_studied_history_book
        )