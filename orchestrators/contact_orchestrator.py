from typing import Union
from sqlalchemy.orm import Session

from decorators.handlers import exception_handler
from dto.dtos import ContactDTO
from models.models import Contact
from services.contact_group_service import ContactGroupService
from services.contact_service import ContactService
from services.contact_tag_service import ContactTagService


class ContactOrchestrator:

    def __init__(self):
        self.contact_service = ContactService()
        self.group_service = ContactGroupService()
        self.tag_service = ContactTagService()

    @exception_handler
    def contact_register_full(
            self,
            data: Union[ContactDTO | dict],
            session: Session
    ) -> Contact:
        contact = self.contact_service.create_contact(data, session, False)
        session.flush()

        for group_id in data.group_ids:
            self.group_service.create_group(group_id, contact.id, session, False)
        contact_id = contact.id
        session.commit()

        return self.contact_service.get_contact(contact_id, session)
