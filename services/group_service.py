from typing import Optional, Union
from uuid import UUID
from sqlalchemy.orm import Session
from abstract.abstracr_group_impl import AbstractGroupImpl
from decorators.handlers import exception_handler
from dto.dtos import GroupDTO
from exceptions.exceptions import NotFound
from models.models import Group
from repositories.group_repository import GroupRepository


class GroupService(AbstractGroupImpl):

    def __init__(
            self,
            repository: GroupRepository = GroupRepository()
    ) -> None:
        self.repository = repository

    @exception_handler
    def create_group(
            self,
            data: Union[GroupDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Group:
        group = Group(**data.model_dump())
        self.repository.create(group, session, auto_commit)
        return group

    @exception_handler
    def get_groups(
            self,
            session: Session
    ) -> list[Group]:
        result = self.repository.select(session)
        return result

    @exception_handler
    def get_group(
            self,
            group_id: UUID,
            session: Session
    ) -> Optional[Group]:
        result = self.repository.get(group_id, session)
        if not result:
            raise NotFound()
        return result

    @exception_handler
    def update_group(
            self,
            group_id: UUID,
            data: Union[GroupDTO | dict],
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Group]:
        result = self.repository.update(group_id, data.model_dump(exclude={"id"}),
                                        session, auto_commit)
        if not result:
            raise NotFound()
        return result

    @exception_handler
    def delete_group(
            self,
            group_id: UUID,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[Group]:
        result = self.repository.delete(group_id, session, auto_commit)
        if not result:
            raise NotFound()
        return result
