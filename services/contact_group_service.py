from uuid import UUID
from sqlalchemy.orm import Session
from abstract.abstract_contact_group_impl import AbstractContactGroupImpl
from models.models import ContactGroup
from repositories.contact_group_repository import ContactGroupRepository


class ContactGroupService(AbstractContactGroupImpl):

    def __init__(
            self,
            repository: ContactGroupRepository = ContactGroupRepository()
    ) -> None:
        self.repository = repository

    def create_group(
            self,
            group_id: UUID,
            contact_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContactGroup:
        contact = ContactGroup(group_id=group_id, contact_id=contact_id)
        self.repository.create(contact, session, auto_commit)
        return contact
