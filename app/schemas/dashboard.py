from datetime import date
from typing import List
from pydantic import BaseModel


class StudyBookProgress(BaseModel):
    study_books_completed_count:  int
    study_books_incomplete_count: int
    start_study_period_on:        date
    end_study_period_on:          date


class StudyTimesByWeek(BaseModel):
    months_and_years:           str
    study_minutes_by_first_week:  int
    study_minutes_by_second_week: int
    study_minutes_by_third_week:  int
    study_minutes_by_fourth_week: int

class StudyTimes(BaseModel):
    study_minutes_total:      int
    study_minutes_by_monthly: List[StudyTimesByWeek]


class BookCountsByShelve(BaseModel):
    shelve_name: str
    books_count: int

class BookCounts(BaseModel):
    books_total_count:      int
    books_count_by_shelve:  List[BookCountsByShelve]
