from typing import Union, Optional
from pydantic import BaseModel, Field


class OutputBook(BaseModel):
    id:           int
    isbn:         Optional[str]
    shelve_name:  str
    title:        str
    remark:       Optional[str]
    img_url:      Optional[str]

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    isbn:         Optional[str] = Field(max_length=13)
    title:        Optional[str] = Field(min_length=1, max_length=50)
    shelve_id:    int
    remark:       Optional[str] = Field(min_length=1, max_length=255)
    img_url:      Optional[str]


class UpdateBook(BaseModel):
    isbn:         Optional[str] = Field(max_length=13)
    title:        str           = Field(min_length=1, max_length=50)
    remark:       Optional[str] = Field(min_length=1, max_length=255)
    img_url:      Optional[str]
