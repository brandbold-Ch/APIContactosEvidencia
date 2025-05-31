from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session
from abstract.abstract_tag_impl import AbstractTagImpl
from models.models import Tag
from repositories.tag_repository import TagRepository


class TagService(AbstractTagImpl):

    def __init__(
            self,
            repository: TagRepository = TagRepository()
    ) -> None:
        self.repository = repository

    def create_tag(
            self,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Tag:
        tag = Tag(*data)
        self.repository.create(tag, session, auto_commit)
        return tag

    def get_tags(
            self,
            session: Session
    ) -> list[Tag]:
        result = self.repository.select(session)
        return result

    def get_tag(
            self,
            tag_id: UUID,
            session: Session
    ) -> Optional[Tag]:
        result = self.repository.get(tag_id, session)
        return result

    def update_tag(
            self,
            tag_id: UUID,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Tag]:
        result = self.repository.update(tag_id, data, session, auto_commit)
        return result

    def delete_tag(
            self,
            tag_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Tag]:
        result = self.repository.delete(tag_id, session, auto_commit)
        return result
