from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.book_repository import BookRepository
from app.schemas.books import OutputBook
from app.database.model.models import User

class BookService:
    def __init__(self, session: Session, user: User):
        self.book_repository = BookRepository(session)
        self.user = user
    

    def individual_book(self, id: int) -> OutputBook:
        book = self.book_repository.user_has_find_by_id(self.user.id, id)
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