from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    name:     str = Field(min_length=1, max_length=50)
    email:    str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=1, max_length=255)


class OutputUser(BaseModel):
    id:       int
    name:     str
    email:    str