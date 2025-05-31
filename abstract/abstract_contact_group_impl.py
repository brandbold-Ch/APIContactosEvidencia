from abc import ABC, abstractmethod
from uuid import UUID
from sqlalchemy.orm import Session
from models.models import ContactGroup


class AbstractContactGroupImpl(ABC):

    @abstractmethod
    def create_group(
            self,
            group_id: UUID,
            contact_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> ContactGroup:
        pass
