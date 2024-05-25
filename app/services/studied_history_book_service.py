from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.repositories.book_repository import BookRepository
from app.repositories.studying_book_repository import StudyingBookRepository
from app.schemas.studied_history_books import ListStudiedHistoryBooks, StudiedHistoryBook, ListStudiedHistories, StudiedHistory
from app.database.model.models import User

class StudiedHistoryBookService:
    def __init__(self, session: Session, user: User):
        self.studying_book_repository = StudyingBookRepository(session)
        self.book_repository = BookRepository(session)
        self.user = user
        self.session = session

    
    def list_studied_history_books(self) -> ListStudiedHistoryBooks:
        studied_history_books = self.book_repository.user_with_complated_in_count_list(self.user.id)

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
    

    def individual_studied_history_book(self, book_id: int):
        studied_histories = self.studying_book_repository.user_with_completed_in_minutes_list_by_book_id(self.user.id, book_id)
        if len(studied_histories) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="書籍履歴が存在しません。"
            )
        
        response_studied_histories = []
        for studied_history in studied_histories:
            response_studied_histories.append(
                StudiedHistory(
                    id=studied_history.StudyingBook.id,
                    start_on=studied_history.StudyingBook.start_on,
                    target_on=studied_history.StudyingBook.target_on,
                    target_items=studied_history.StudyingBook.target_items,
                    memo=studied_history.StudyingBook.memo,
                    study_minutes=studied_history.study_minutes
                )
            )

        return response_studied_histories
        