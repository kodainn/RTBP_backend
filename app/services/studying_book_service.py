from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List

from app.repositories.book_repository import BookRepository
from app.repositories.studying_book_repository import StudyingBookRepository
from app.repositories.target_item_repository import TargetItemRepository
from app.schemas.studying_books import CreateStudyingBook, ListStudyingBooks, StudyingBookInList, OutputStudyingBook
from app.database.model.models import User

class StudyingBookService:
    def __init__(self, session: Session, user: User):
        self.book_repository = BookRepository(session)
        self.studying_book_repository = StudyingBookRepository(session)
        self.target_item_repository = TargetItemRepository(session)
        self.user = user
        self.session = session


    def list_studying_books(self) -> ListStudyingBooks:
        studying_books = self.studying_book_repository.user_has_incompleted_list(self.user.id)

        response_studying_books = []
        for studying_book in studying_books:
            response_studying_books.append(
                StudyingBookInList(
                    id=studying_book.id,
                    title=studying_book.book.title,
                    img_url=studying_book.book.img_url,
                    start_on=studying_book.start_on,
                    target_on=studying_book.target_on
                )
            )
        
        return ListStudyingBooks(
            studying_books=response_studying_books
        )
    

    def individual_studying_book(self, id: int) -> OutputStudyingBook:
        studying_book = self.studying_book_repository.user_has_incompleted_individual(self.user.id, id)
        if studying_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その学習書籍は存在しません。"
            )
        
        return OutputStudyingBook(
            id=studying_book.id,
            start_on=studying_book.start_on,
            target_on=studying_book.target_on,
            target_items=studying_book.target_items
        )


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
    

    def delete(self, id: int) -> None:
        studying_book = self.studying_book_repository.user_has_find_by_id(self.user.id, id)
        if studying_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その書籍を存在しません。"
            )
        
        self.studying_book_repository.delete(self.user.id, id)

        return