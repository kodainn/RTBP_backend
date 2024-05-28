from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.book_repository import BookRepository
from app.repositories.studying_book_repository import StudyingBookRepository
from app.repositories.target_item_repository import TargetItemRepository
from app.repositories.study_track_repository import StudyTrackRepository
from app.schemas.studying_books import CreateStudyingBook, ListStudyingBooks, StudyingBookInList, OutputStudyingBook, CreateStudyingBookRecord, Book, StudyingBook, IndividualStudyingBook
from app.database.model.models import User

class StudyingBookService:
    def __init__(self, session: Session, user: User):
        self.book_repository = BookRepository(session)
        self.studying_book_repository = StudyingBookRepository(session)
        self.target_item_repository = TargetItemRepository(session)
        self.study_track_repository = StudyTrackRepository(session)
        self.user = user
        self.session = session


    def list_studying_books(self) -> ListStudyingBooks:
        studying_books = self.studying_book_repository.user_with_incompleted_list(self.user.id)

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
    

    def individual_studying_book(self, id: int) -> IndividualStudyingBook:
        studying_book = self.studying_book_repository.user_with_incompleted_individual(self.user.id, id)
        if studying_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Study book not found."
            )
        
        book = Book(
            id=studying_book.book.id,
            shelve_name=studying_book.book.shelve.name,
            title=studying_book.book.title,
            remark=studying_book.book.remark,
            img_url=studying_book.book.img_url
        )

        studying_book = StudyingBook(
            id=studying_book.id,
            start_on=studying_book.start_on,
            target_on=studying_book.target_on,
            memo=studying_book.memo,
            target_items=studying_book.target_items
        )
        
        return IndividualStudyingBook(
            book=book,
            studying_book=studying_book
        )


    def create(self, req_body: CreateStudyingBook) -> OutputStudyingBook:        
        try:
            with self.session.begin():
                book = self.book_repository.user_with_find_by_id(self.user.id, req_body.book_id)
                if book is None:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found."
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
            memo=studying_book.memo,
            target_items=studying_book.target_items,
            study_tracks=studying_book.study_tracks
        )
    
    
    
    def create_record(self, id: int, req_body: CreateStudyingBookRecord) -> OutputStudyingBook:

        try:
            with self.session.begin():
                studying_book = self.studying_book_repository.user_with_incompleted_individual(self.user.id, id)
                if studying_book is None:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Study book not found."
                    )
                
                #学習完了か判定
                is_all_complated = True
                for target_completed in req_body.target_complate_items:
                    if not target_completed.is_completed:
                        is_all_complated = False
                        break

                updated_studying_book = self.studying_book_repository.update_memo_and_is_completed(self.user.id, id, req_body.memo, is_all_complated)
                self.target_item_repository.update(id, req_body)
                self.study_track_repository.create(id, req_body)
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
        self.session.commit()

        return OutputStudyingBook(
            id=studying_book.id,
            start_on=studying_book.start_on,
            target_on=studying_book.target_on,
            memo=updated_studying_book.memo,
            target_items=studying_book.target_items,
            study_tracks=studying_book.study_tracks
        )
    

    def delete(self, id: int) -> None:
        studying_book = self.studying_book_repository.user_with_find_by_id(self.user.id, id)
        if studying_book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Book not found."
            )
        
        self.studying_book_repository.delete(self.user.id, id)

        return