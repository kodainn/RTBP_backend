import copy

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.shelves import ListShelves, CreateShelve, OutputShelve, UpdateShelve, ShelveInListBooks
from app.database.model.models import User
from app.repositories.shelve_repository import ShelveRepository
from app.repositories.studying_book_repository import StudyingBookRepository
from app.repositories.book_repository import BookRepository


class ShelveService:
    def __init__(self, session: Session, user: User):
        self.shelve_repository = ShelveRepository(session)
        self.studying_book_repository = StudyingBookRepository(session)
        self.book_repository = BookRepository(session)
        self.user = user


    def list_shelves(self, title: str) -> ListShelves:
        shelves = self.shelve_repository.user_with_list_in_book_like_title(self.user.id, title)

        for shelve in shelves:
            filter_books = []
            for book in shelve.books:
                if title in book.title:
                    filter_books.append(book)
            shelve.books = filter_books

        return ListShelves(
            shelves=shelves
        )
    

    def individual_shelve(self, id: int) -> OutputShelve:
        shelve = self.shelve_repository.user_with_individual_by_id(self.user.id, id)
        if shelve is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bookshelf not found."
            )
        
        return OutputShelve(
            id=shelve.id,
            name=shelve.name
        )
    

    def shelve_in_list_books(self, id: int) -> ShelveInListBooks:
        shelve_in_books = self.shelve_repository.user_with_shelve_in_books(self.user.id, id)
        if shelve_in_books is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bookshelf not found."
            )
        
        return ShelveInListBooks(
            id=shelve_in_books.id,
            name=shelve_in_books.name,
            books=shelve_in_books.books
        )



    def create(self, req_body: CreateShelve) -> OutputShelve:
        has_shelve = self.shelve_repository.user_with_has_shelve_by_name(self.user.id, req_body.name)
        if has_shelve:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="The shelf name is already registered."
            )

        shelve = self.shelve_repository.create(self.user.id, req_body)

        return OutputShelve(
            id=shelve.id,
            name=shelve.name
        )
    

    def update(self, id: int, req_body: UpdateShelve) -> OutputShelve:
        shelve = self.shelve_repository.user_with_individual_by_id(self.user.id, id)
        if shelve is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bookshelf not found."
            )

        updated_shelve = self.shelve_repository.update(self.user.id, id, req_body)

        return OutputShelve(
            id=updated_shelve.id,
            name=updated_shelve.name
        )
    

    def delete(self, id: int) -> None:
        shelve = self.shelve_repository.user_with_individual_by_id(self.user.id, id)
        if shelve is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Bookshelf not found."
            )
        
        self.shelve_repository.delete(id, self.user.id)

