from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.book_repository import BookRepository
from app.repositories.studying_book_repository import StudyingBookRepository
from app.repositories.target_item_repository import TargetItemRepository
from app.schemas.studying_books import CreateStudyingBook, OutputStudyingBook
from app.database.model.models import User

class StudyingBookService:
    def __init__(self, session: Session, user: User):
        self.book_repository = BookRepository(session)
        self.studying_book_repository = StudyingBookRepository(session)
        self.target_item_repository = TargetItemRepository(session)
        self.user = user
        self.session = session
    

    def create(self, req_body: CreateStudyingBook) -> OutputStudyingBook:        
        try:
            with self.session.begin():
                book = self.book_repository.user_has_find_by_id(self.user.id, req_body.book_id)
                if book is None:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="その書籍は存在しません。"
                    )
                
                studying_book = self.studying_book_repository.create(self.user.id, req_body)
                self.target_item_repository.create(studying_book.id, req_body)
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        

        return OutputStudyingBook(
            id=studying_book.id,
            start_on=studying_book.start_on,
            target_on=studying_book.target_on,
            target_items=studying_book.target_items
        )

