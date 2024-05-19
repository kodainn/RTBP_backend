from fastapi import APIRouter, Depends
import app.schemas.shelves as schema
from app.utils.auth import oauth2_scheme

router = APIRouter()

@router.get("/shelves", response_model=schema.ListShelves)
async def list_shelves(access_token: str = Depends(oauth2_scheme)):
    pass


@router.get("/shelves/{id}", response_model=schema.Shelve)
async def individual_shelve(access_token: str = Depends(oauth2_scheme)):
    pass


@router.get("/shelves/{id}/books", response_model=schema.ShelveInListBooks)
async def shelve_in_list_books(access_token: str = Depends(oauth2_scheme)):
    pass


@router.post("/shelves")
async def create_shelve(req_body: schema.CreateShelve, access_token: str = Depends(oauth2_scheme)):
    pass


@router.patch("/shelves/{id}")
async def update_shelve(req_body: schema.UpdateShelve, access_token: str = Depends(oauth2_scheme)):
    pass


@router.delete("/shelves/{id}")
async def delete_shelve(access_token: str = Depends(oauth2_scheme)):
    pass