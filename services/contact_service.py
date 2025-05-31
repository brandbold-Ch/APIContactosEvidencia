from typing import Optional, Union
from uuid import UUID
from sqlalchemy.orm import Session
from abstract.abstract_contact_impl import AbstractContactImpl
from decorators.handlers import exception_handler
from exceptions.exceptions import NotFound
from models.models import Contact
from repositories.contact_repository import ContactRepository
from dto.dtos import ContactDTO


class ContactService(AbstractContactImpl):

    def __init__(
            self,
            repository: ContactRepository = ContactRepository()
    ) -> None:
        self.repository = repository

    @exception_handler
    def create_contact(
            self,
            data: Union[ContactDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Contact:
        contact = Contact(**data.model_dump(exclude={"group_ids"}))
        self.repository.create(contact, session, auto_commit)
        return contact

    @exception_handler
    def get_contacts(
            self,
            session: Session
    ) -> list[Contact]:
        result = self.repository.select(session)
        return result

    @exception_handler
    def get_contact(
            self,
            contact_id: UUID,
            session: Session
    ) -> Optional[Contact]:
        result = self.repository.get(contact_id, session)
        if not result:
            raise NotFound()
        return result

    @exception_handler
    def update_contact(
            self,
            contact_id: UUID,
            data: Union[ContactDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Contact]:
        result = self.repository.update(contact_id, data.model_dump(exclude={"id"}),
                                        session, auto_commit)
        if not result:
            raise NotFound()
        return result

    @exception_handler
    def delete_contact(
            self,
            contact_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Contact]:
        result = self.repository.delete(contact_id, session, auto_commit)
        if not result:
            raise NotFound()
        return result
