from typing import Annotated, List
from uuid import UUID
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from config.orm import get_session
from dto.dtos import GroupDTO
from services.group_service import GroupService

group_controller = APIRouter(prefix="/groups")
service = GroupService()


@group_controller.post("/", response_model=GroupDTO)
def create_group(
        group: GroupDTO,
        session: Session = Depends(get_session)
) -> GroupDTO:
    result = service.create_group(group, session)
    return result


@group_controller.get("/{group_id}", response_model=GroupDTO)
def get_group(
        group_id: Annotated[UUID, Path(...)],
        session: Session = Depends(get_session)
) -> GroupDTO:
    result = service.get_group(group_id, session)
    return result


@group_controller.get("/", response_model=List[GroupDTO])
def get_groups(
        session: Session = Depends(get_session)
) -> List[GroupDTO]:
    result = service.get_groups(session)
    return result


@group_controller.delete("/{group_id}", response_model=GroupDTO)
def delete_group(
        group_id: Annotated[UUID, Path(...)],
        session: Session = Depends(get_session)
) -> GroupDTO:
    result = service.delete_group(group_id, session)
    return result


@group_controller.put("/{group_id}", response_model=GroupDTO)
def update_group(
        group_id: Annotated[UUID, Path(...)],
        group: GroupDTO,
        session: Session = Depends(get_session)
) -> GroupDTO:
    result = service.update_group(group_id, group, session)
    return result
