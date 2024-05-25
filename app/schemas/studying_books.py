from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field


class StudyingBookInList(BaseModel):
    id:        int
    title:     str
    img_url:   str
    start_on:  date
    target_on: date

    class Config:
        orm_mode = True


class ListStudyingBooks(BaseModel):
    studying_books: List[StudyingBookInList]


class TargetItem(BaseModel):
    id:           int
    description:  str
    is_completed: bool

    class Config:
        orm_mode = True


class StudyTrack(BaseModel):
    id:               int
    minutes:          int
    study_on:         date
    studying_book_id: int

    class Config:
        orm_mode = True


class OutputStudyingBook(BaseModel):
    id:           int
    start_on:     date
    target_on:    date
    memo:         Optional[str]
    target_items: List[TargetItem]
    study_tracks: List[Optional[StudyTrack]]
    
    class Config:
        orm_mode = True


class CrateTargetItem(BaseModel):
    description: str = Field(min_length=1, max_length=255)

    
class CreateStudyingBook(BaseModel):
    book_id:      int
    target_items: List[CrateTargetItem]
    target_on:    date


class CreateComplateTargetItem(BaseModel):
    id:           int
    is_completed: bool


class CreateStudyingBookRecord(BaseModel):
    target_complate_items: List[CreateComplateTargetItem]
    memo:                  Optional[str] = Field(max_length=255)
    study_minutes:         int