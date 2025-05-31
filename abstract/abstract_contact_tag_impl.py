from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.orm import Session
from models.models import ContactGroup


class AbstractContactTagImpl(ABC):

    @abstractmethod
    def create_tag(
            self,
            tag_id: UUID,
            contact_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContactGroup:
        pass
