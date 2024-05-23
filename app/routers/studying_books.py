from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas.studying_books import ListStudyingBooks, OutputStudyingBook, CreateStudyingBook, CreateStudyingBookRecord
from app.services.studying_book_service import StudyingBookService
from app.database.config.connect import get_db
from app.database.model.models import User



router = APIRouter()

@router.get("/studying-books", response_model=ListStudyingBooks)
async def list_studying_books(session: Session = Depends(get_db)):
    user = User(id=10, name="Tanaka",email="Tanaka@example.com",password="password")
    studying_books = StudyingBookService(session, user).list_studying_books()

    return studying_books


@router.get("/studying-books/{id}", response_model=OutputStudyingBook)
async def individual_studying_book():
    pass


@router.post("/studying-books", response_model=OutputStudyingBook, status_code=status.HTTP_201_CREATED)
async def create_studying_book(req_body: CreateStudyingBook, session: Session = Depends(get_db)):
    user = User(id=1, name="Tanaka",email="Tanaka@example.com",password="password")
    studying_book = StudyingBookService(session, user).create(req_body)

    return studying_book


@router.delete("/studying-books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_studying_book(id: int, session: Session = Depends(get_db)):
    user = User(id=1, name="Tanaka",email="Tanaka@example.com",password="password")
    StudyingBookService(session, user).delete(id)

    return


@router.post("/studying-books/{id}/record")
async def create_studying_book_record(req_body: CreateStudyingBookRecord, ):
    pass
