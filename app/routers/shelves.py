from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Optional

from app.schemas.shelves import ListShelves, OutputShelve, ShelveInListBooks, CreateShelve, UpdateShelve
from app.database.model.models import User
from app.database.config.connect import get_db
from app.services.shelve_service import ShelveService
from app.utils.auth import get_current_user

router = APIRouter()

@router.get("/shelves", response_model=ListShelves)
async def list_shelves(title: str = "", session: Session = Depends(get_db), user = Depends(get_current_user)):
    shelves = ShelveService(session, user).list_shelves(title)

    return shelves



@router.get("/shelves/{id}", response_model=OutputShelve)
async def individual_shelve(id: int, session: Session = Depends(get_db), user = Depends(get_current_user)):
    shelve = ShelveService(session, user).individual_shelve(id)
    
    return shelve


@router.get("/shelves/{id}/books", response_model=ShelveInListBooks)
async def shelve_in_list_books(id: int, session: Session = Depends(get_db), user = Depends(get_current_user)):
    shelve_in_books = ShelveService(session, user).shelve_in_list_books(id)
    
    return shelve_in_books


@router.post("/shelves", status_code=status.HTTP_201_CREATED, response_model=OutputShelve)
async def create_shelve(req_body: CreateShelve, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    shelve = ShelveService(session, user).create(req_body)
    return shelve


@router.patch("/shelves/{id}", response_model=OutputShelve)
async def update_shelve(id: int, req_body: UpdateShelve, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    shelve = ShelveService(session, user).update(id, req_body)
    return shelve


@router.delete("/shelves/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_shelve(id: int, session: Session = Depends(get_db), user: User = Depends(get_current_user)):
    ShelveService(session, user).delete(id)

    return