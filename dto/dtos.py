from datetime import date
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr


class GroupDTO(BaseModel):
    id: UUID = Field(default_factory=lambda: uuid4())
    group_name: str
    contacts: List["ContactSummaryDTO"] = []


class ContactSummaryDTO(BaseModel):
    id: UUID = Field(default_factory=lambda: uuid4())
    name: str
    last_name: Optional[str]
    business: Optional[str]
    phone_number: str = Field(max_length=10)
    email: Optional[EmailStr]
    birth_date: Optional[date]

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True


class GroupSummaryDTO(BaseModel):
    id: UUID
    group_name: str


class ContactDTO(BaseModel):
    id: UUID = Field(default_factory=lambda: uuid4())
    name: str
    last_name: Optional[str]
    business: Optional[str]
    phone_number: str = Field(max_length=10)
    email: Optional[EmailStr]
    birth_date: Optional[date]
    group_ids: List[UUID] = []
    groups: List[GroupSummaryDTO] = []

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
