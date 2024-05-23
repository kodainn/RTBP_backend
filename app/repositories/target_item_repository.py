from typing import Dict, Optional, Union
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import TargetItem
from app.schemas.studying_books import CreateStudyingBook



class TargetItemRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def create(self, studying_book_id: int, create_studying_book: CreateStudyingBook) -> None:
        create_target_items = []
        for create_target_item in create_studying_book.target_items:
            create_target_items.append({
                    "description": create_target_item.description,
                    "studying_book_id": studying_book_id
                })
        
        self.session.bulk_insert_mappings(TargetItem, create_target_items)

        return