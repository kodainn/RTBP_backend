from typing import List, Optional
from pydantic import BaseModel, Field

class OutputShelve(BaseModel):
    id:   int
    name: str

    class Config:
        orm_mode = True


class Book(BaseModel):
    id:      int
    title:   str
    img_url: Optional[str]

    class Config:
        orm_mode = True


class ShelveInListBooks(BaseModel):
    id:    int
    name:  str
    books: List[Book]

    class Config:
        orm_mode = True


class ListShelves(BaseModel):
    shelves: List[Optional[ShelveInListBooks]]


class CreateShelve(BaseModel):
    name: str = Field(min_length=1, max_length=50)


class UpdateShelve(BaseModel):
    name: str = Field(min_length=1, max_length=50)