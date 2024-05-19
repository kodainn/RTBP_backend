from fastapi import APIRouter, Depends
import app.schemas.studying_books as schema
from app.utils.auth import oauth2_scheme

router = APIRouter()

@router.get("/studying-books", response_model=schema.ListStudyingBooks)
async def list_studying_books(access_token: str = Depends(oauth2_scheme)):
    pass


@router.get("/studying-books/{id}", response_model=schema.IndividualStudyingBook)
async def individual_studying_book(access_token: str = Depends(oauth2_scheme)):
    pass


@router.post("/studying-books")
async def create_studying_book(req_body: schema.CreateStudyingBook, access_token: str = Depends(oauth2_scheme)):
    pass


@router.delete("/studying-books/{id}")
async def delete_studying_book(access_token: str = Depends(oauth2_scheme)):
    pass


@router.post("/studying-books/{id}/record")
async def create_studying_book_record(req_body: schema.CreateStudyingBookRecord, access_token: str = Depends(oauth2_scheme)):
    pass
