from fastapi import APIRouter, Depends
import app.schemas.shelves as schema
from app.utils.auth import oauth2_scheme

router = APIRouter()

@router.get("/shelves", response_model=schema.ListShelves)
async def list_shelves():
    pass


@router.get("/shelves/{id}", response_model=schema.Shelve)
async def individual_shelve():
    pass


@router.get("/shelves/{id}/books", response_model=schema.ShelveInListBooks)
async def shelve_in_list_books():
    pass


@router.post("/shelves")
async def create_shelve(req_body: schema.CreateShelve, ):
    pass


@router.patch("/shelves/{id}")
async def update_shelve(req_body: schema.UpdateShelve, ):
    pass


@router.delete("/shelves/{id}")
async def delete_shelve():
    pass