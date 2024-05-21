from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.dashboard import StudyBookProgress, StudyTimes, BookCounts
from app.database.config.connect import get_db
from app.services.dashboard_service import DashboardService
from app.database.model.models import User

router = APIRouter()

@router.get("/dashboard/study-book-progress", response_model=StudyBookProgress)
async def study_book_progress(session: Session = Depends(get_db)):
    user = User(id=1,name="Tanaka",email="Tanaka@example.com",password="password")
    progress = DashboardService(session, user).studying_book_progress()
    return progress


@router.get("/dashboard/study-times", response_model=StudyTimes)
async def study_times(session: Session = Depends(get_db)):
    user = User(id=1,name="Tanaka",email="Tanaka@example.com",password="password")
    study_times = DashboardService(session, user).study_times()
    return study_times


@router.get("/dashboard/book-counts", response_model=BookCounts)
async def book_counts(session: Session = Depends(get_db)):
    user = User(id=1,name="Tanaka",email="Tanaka@example.com",password="password")
    book_counts = DashboardService(session, user).book_counts()
    return book_counts