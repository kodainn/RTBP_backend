from typing import Dict, Optional, Union
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.model.models import TargetItem
from app.schemas.studying_books import CreateStudyingBook, CreateStudyingBookRecord 



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
    

    def update(self, studying_book_id: int, create_studying_book_record :CreateStudyingBookRecord) -> None:
        query = self.session.query(TargetItem)
        query = query.filter_by(studying_book_id=studying_book_id)

        result = query.all()
        regular_id_list = [res.id for res in result]

        complate_target_items = []
        for target_complate_item in create_studying_book_record.target_complate_items:
            # 目標達成が完了になるもののみ更新対象とする、不正なIDによる更新をさせない
            if not target_complate_item.is_completed or target_complate_item.id not in regular_id_list:
                continue

            complate_target_items.append({
                "id": target_complate_item.id,
                "is_completed": True
            })
        
        self.session.bulk_update_mappings(TargetItem, complate_target_items)

        return