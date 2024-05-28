from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.books import OutputBook, CreateBook, UpdateBook
from app.database.config.connect import get_db
from app.database.model.models import User
from app.services.book_service import BookService
from app.utils.auth import get_current_user

router = APIRouter()


@router.get("/books/{id}", response_model=OutputBook)
async def individual_book(id: int, session: Session = Depends(get_db), user = Depends(get_current_user)):
    book = BookService(session, user).individual_book(id)
    
    return book


@router.post("/books", status_code=status.HTTP_201_CREATED, response_model=OutputBook)
async def create_book(req_body: CreateBook, session: Session = Depends(get_db), user = Depends(get_current_user)):
    book = BookService(session, user).create(req_body)

    return book


@router.patch("/books/{id}", response_model=OutputBook)
async def update_book(id: int, req_body: UpdateBook, session: Session = Depends(get_db), user = Depends(get_current_user)):
    book = BookService(session, user).update(id, req_body)

    return book


@router.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int, session: Session = Depends(get_db), user = Depends(get_current_user)):
    BookService(session, user).delete(id)

    return
