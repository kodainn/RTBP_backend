from fastapi import APIRouter
import app.schemas.studying_books as schema # type: ignore

router = APIRouter()

@router.get("/studying-books", response_model=schema.ListStudyingBooks)
async def list_studying_books():
    pass


@router.get("/studying-books/{id}", response_model=schema.IndividualStudyingBook)
async def individual_studying_book():
    pass


@router.post("/studying-books")
async def create_studying_book(req_body: schema.CreateStudyingBook):
    pass


@router.delete("/studying-books/{id}")
async def delete_studying_book():
    pass


@router.post("/studying-books/{id}/record")
async def create_studying_book_record(req_body: schema.CreateStudyingBookRecord):
    pass