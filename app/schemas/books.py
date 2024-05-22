from typing import Union, Optional
from pydantic import BaseModel


class OutputBook(BaseModel):
    id:           int
    isbn:         Optional[int]
    shelve_name:  str
    title:        str
    remark:       Union[str, None]
    img_url:      Union[str, None]

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    isbn:         Optional[int]
    title:        str
    shelve_id:    int
    remark:       Union[str, None]
    img_url:      Union[str, None]


class UpdateBook(BaseModel):
    isbn:         Optional[int]
    title:        str
    remark:       Union[str, None]
    img_url:      Union[str, None]
