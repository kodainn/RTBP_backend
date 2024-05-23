from datetime import date
from typing import List
from pydantic import BaseModel


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
    is_complated: bool

    class Config:
        orm_mode = True

class OutputStudyingBook(BaseModel):
    id:           int
    start_on:     date
    target_on:    date
    target_items: List[TargetItem]

    class Config:
        orm_mode = True


class CrateTargetItem(BaseModel):
    description: str

    
class CreateStudyingBook(BaseModel):
    book_id:      int
    target_items: List[CrateTargetItem]
    target_on:    date


class CreateComplateTargetItem(BaseModel):
    id:           int
    is_complated: bool


class CreateStudyingBookRecord(BaseModel):
    target_complate_items: List[CreateComplateTargetItem]
    study_minutes:  int