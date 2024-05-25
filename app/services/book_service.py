from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.book_repository import BookRepository
from app.repositories.shelve_repository import ShelveRepository
from app.schemas.books import OutputBook, CreateBook, UpdateBook
from app.database.model.models import User

class BookService:
    def __init__(self, session: Session, user: User):
        self.book_repository = BookRepository(session)
        self.shelve_repository = ShelveRepository(session)
        self.user = user
    

    def individual_book(self, id: int) -> OutputBook:
        book = self.book_repository.user_with_find_by_id(self.user.id, id)
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その本棚は存在しません。"
            )
        
        return OutputBook(
            id=book.id,
            isbn=book.isbn,
            shelve_name=book.shelve.name,
            title=book.title,
            remark=book.remark,
            img_url=book.img_url
        )
    

    def create(self, req_body: CreateBook) -> OutputBook:
        has_book = self.book_repository.user_with_has_book_by_title(self.user.id, req_body.title)
        if has_book:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="その書籍名は既に登録されています。"
            )
        
        shelve = self.shelve_repository.user_with_individual_by_id(self.user.id, req_body.shelve_id)
        if shelve is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その本棚は存在しません。"
            )
        
        create_book = self.book_repository.create(self.user.id, req_body)

        return OutputBook(
            id=create_book.id,
            isbn=create_book.isbn,
            shelve_name=create_book.shelve.name,
            title=create_book.title,
            remark=create_book.remark,
            img_url=create_book.img_url
        )
    

    def update(self, id: int, req_body: UpdateBook) -> OutputBook:
        book = self.book_repository.user_with_individual_by_id(self.user.id, id)
        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その本棚は存在しません。"
            )
        
        has_some_book = self.book_repository.user_with_has_some_book_by_title(self.user.id, id, req_body.title)
        if has_some_book:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="その書籍名は既に登録されています。"
            )

        updated_book = self.book_repository.update(self.user.id, id, req_body)

        return OutputBook(
            id=updated_book.id,
            isbn=updated_book.isbn,
            title=updated_book.title,
            shelve_name=updated_book.shelve.name,
            remark=updated_book.remark,
            img_url=updated_book.img_url,
        )
    

    def delete(self, id: int) -> None:
        shelve = self.book_repository.user_with_find_by_id(self.user.id, id)
        if shelve is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="その書籍は存在しません。"
            )
        
        self.book_repository.delete(self.user.id, id)