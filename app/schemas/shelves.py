from typing import Union, List
from pydantic import BaseModel

class Shelve(BaseModel):
    id:   int
    name: str

class Book(BaseModel):
    id:      int
    title:   str
    img_url: str

class ShelveInListBooks(BaseModel):
    id:    int
    name:  str
    books: List[Book]


class ListShelves(BaseModel):
    shelves: List[ShelveInListBooks]


class CreateShelve(BaseModel):
    name: str


class UpdateShelve(BaseModel):
    id:   int
    name: str