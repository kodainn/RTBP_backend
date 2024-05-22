from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.books import OutputBook, CreateBook, UpdateBook
from app.database.config.connect import get_db
from app.database.model.models import User
from app.services.book_service import BookService

router = APIRouter()


@router.get("/books/{id}", response_model=OutputBook)
async def individual_book(id: int, session: Session = Depends(get_db)):
    user = User(id=1,name="Tanaka",email="Tanaka@example.com",password="password")
    book = BookService(session, user).individual_book(id)
    
    return book


@router.post("/books")
async def create_book(req_body: CreateBook):
    pass


@router.patch("/books/{id}")
async def update_book(req_body: UpdateBook):
    pass


@router.delete("/books/{id}")
async def delete_book():
    pass
