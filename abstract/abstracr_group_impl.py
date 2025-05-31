from abc import ABC, abstractmethod
from typing import Optional, Union
from uuid import UUID
from sqlalchemy.orm import Session

from dto.dtos import GroupDTO
from models.models import Group


class AbstractGroupImpl(ABC):

    @abstractmethod
    def create_group(
            self,
            data: Union[GroupDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Group:
        pass

    @abstractmethod
    def get_groups(
            self,
            session: Session
    ) -> list[Group]:
        pass

    @abstractmethod
    def get_group(
            self,
            group_id: UUID,
            session: Session
    ) -> Optional[Group]:
        pass

    @abstractmethod
    def update_group(
            self,
            group_id: UUID,
            data: Union[GroupDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Group]:
        pass

    @abstractmethod
    def delete_group(
            self,
            group_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Group]:
        pass
