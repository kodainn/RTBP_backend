from fastapi import APIRouter, Depends

import app.schemas.books as schema
from app.utils.auth import oauth2_scheme
from app.utils.auth import get_current_user

router = APIRouter()


@router.get("/books/{id}", response_model=schema.Book)
async def individual_book():
    pass


@router.post("/books")
async def create_book(req_body: schema.CreateBook):
    pass


@router.patch("/books/{id}")
async def update_book(req_body: schema.UpdateBook):
    pass


@router.delete("/books/{id}")
async def delete_book():
    pass