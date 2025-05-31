from uuid import UUID
from sqlalchemy.orm import Session
from abstract.abstract_contact_tag_impl import AbstractContactTagImpl
from models.models import ContactTag
from repositories.contact_group_repository import ContactGroupRepository


class ContactTagService(AbstractContactTagImpl):

    def __init__(
            self,
            repository: ContactGroupRepository = ContactGroupRepository()
    ) -> None:
        self.repository = repository

    def create_tag(
            self,
            tag_id: UUID,
            contact_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContactTag:
        tag = ContactTag(tag_id=tag_id, contact_id=contact_id)
        self.repository.create(tag, session, auto_commit)
        return tag
