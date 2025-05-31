from abc import ABC, abstractmethod
from typing import Optional, Union
from uuid import UUID
from sqlalchemy.orm import Session
from dto.dtos import ContactDTO


class AbstractContactImpl(ABC):

    @abstractmethod
    def create_contact(
            self,
            data: Union[ContactDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> ContactDTO:
        pass

    @abstractmethod
    def get_contacts(
            self,
            session: Session
    ) -> list[ContactDTO]:
        pass

    @abstractmethod
    def get_contact(
            self,
            contact_id: UUID,
            session: Session
    ) -> Optional[ContactDTO]:
        pass

    @abstractmethod
    def update_contact(
            self,
            contact_id: UUID,
            data: Union[ContactDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Optional[ContactDTO]:
        pass

    @abstractmethod
    def delete_contact(
            self,
            contact_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[ContactDTO]:
        pass
