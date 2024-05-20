from pydantic import BaseModel

class CreateUser(BaseModel):
    name:     str
    email:    str
    password: str


class OutputUser(BaseModel):
    id:       int
    name:     str
    email:    str