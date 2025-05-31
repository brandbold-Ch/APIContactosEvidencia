from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session
from models.contact_model import Tag


class AbstractTagImpl(ABC):

    @abstractmethod
    def create_tag(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Tag:
        pass

    @abstractmethod
    def get_tags(
            self,
            session: Session
    ) -> list[Tag]:
        pass

    @abstractmethod
    def get_tag(
            self,
            tag_id: UUID,
            session: Session
    ) -> Optional[Tag]:
        pass

    @abstractmethod
    def update_tag(
            self,
            tag_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Tag]:
        pass

    @abstractmethod
    def delete_tag(
            self,
            tag_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Tag]:
        pass
