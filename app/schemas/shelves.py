from typing import List, Optional
from pydantic import BaseModel

class Shelve(BaseModel):
    id:   int
    name: str

    class Config:
        orm_mode = True


class Book(BaseModel):
    id:      int
    title:   str
    img_url: str

    class Config:
        orm_mode = True


class ShelveInListBooks(BaseModel):
    id:    int
    name:  str
    books: List

    class Config:
        orm_mode = True


class ListShelves(BaseModel):
    shelves: List[Optional[ShelveInListBooks]]


class CreateShelve(BaseModel):
    name: str


class UpdateShelve(BaseModel):
    id:   int
    name: str