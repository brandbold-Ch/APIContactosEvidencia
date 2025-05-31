from typing import Annotated, List
from uuid import UUID
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from config.orm import get_session
from dto.dtos import ContactDTO
from orchestrators.contact_orchestrator import ContactOrchestrator
from services.contact_service import ContactService

contact_controller = APIRouter(prefix="/contacts")
orchestrator = ContactOrchestrator()
service = ContactService()


@contact_controller.post("/", response_model=ContactDTO)
def create_contact(
        contact: ContactDTO,
        session: Session = Depends(get_session)
) -> ContactDTO:
    result = orchestrator.contact_register_full(contact, session)
    return result


@contact_controller.get("/{contact_id}", response_model=ContactDTO)
def get_contact(
        contact_id: Annotated[UUID, Path(...)],
        session: Session = Depends(get_session)
) -> ContactDTO:
    result = service.get_contact(contact_id, session)
    return result


@contact_controller.get("/", response_model=List[ContactDTO])
def get_contacts(
        session: Session = Depends(get_session)
) -> List[ContactDTO]:
    result = service.get_contacts(session)
    return result


@contact_controller.delete("/{contact_id}", response_model=ContactDTO)
def delete_contact(
        contact_id: Annotated[UUID, Path(...)],
        session: Session = Depends(get_session)
) -> ContactDTO:
    result = service.delete_contact(contact_id, session)
    return result


@contact_controller.put("/{contact_id}", response_model=ContactDTO)
def update_contact(
        contact_id: Annotated[UUID, Path(...)],
        contact: ContactDTO,
        session: Session = Depends(get_session)
) -> ContactDTO:
    result = service.update_contact(contact_id, contact, session)
    return result
