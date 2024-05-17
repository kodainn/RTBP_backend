from fastapi import APIRouter
import app.schemas.dashboard as schema # type: ignore

router = APIRouter()

@router.get("/dashboard/study-book-progress", response_model=schema.StudyBookProgress)
async def study_book_progress():
    pass


@router.get("/dashboard/study-times", response_model=schema.StudyTimes)
async def study_times():
    pass


@router.get("/dashboard/book-counts", response_model=schema.BookCounts)
async def book_counts():
    pass