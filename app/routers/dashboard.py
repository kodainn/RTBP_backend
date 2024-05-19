from fastapi import APIRouter, Depends
import app.schemas.dashboard as schema
from app.utils.auth import oauth2_scheme

router = APIRouter()

@router.get("/dashboard/study-book-progress", response_model=schema.StudyBookProgress)
async def study_book_progress(access_token: str = Depends(oauth2_scheme)):
    pass


@router.get("/dashboard/study-times", response_model=schema.StudyTimes)
async def study_times(access_token: str = Depends(oauth2_scheme)):
    pass


@router.get("/dashboard/book-counts", response_model=schema.BookCounts)
async def book_counts(access_token: str = Depends(oauth2_scheme)):
    pass