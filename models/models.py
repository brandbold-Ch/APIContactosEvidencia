from datetime import date
from typing import Optional, List
from uuid import UUID, uuid4
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contact"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    last_name: Mapped[Optional[str]]
    business: Mapped[Optional[str]]
    phone_number: Mapped[str] = mapped_column(String(10))
    email: Mapped[Optional[str]]
    birth_date: Mapped[Optional[date]]
    groups: Mapped[List["Group"]] = relationship(back_populates="contacts", secondary="contact_group")
    tags: Mapped[List["Tag"]] = relationship(back_populates="contacts", secondary="contact_tag")

    def fromkeys(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


class Group(Base):
    __tablename__ = "group"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    group_name: Mapped[str]
    contacts: Mapped[List["Contact"]] = relationship(back_populates="groups", secondary="contact_group")

    def fromkeys(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


class Tag(Base):
    __tablename__ = "tag"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    tag_name: Mapped[str]
    contacts: Mapped[List["Contact"]] = relationship(back_populates="tags", secondary="contact_tag")


class ContactGroup(Base):
    __tablename__ = "contact_group"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    group_id: Mapped[UUID] = mapped_column(ForeignKey("group.id"))
    contact_id: Mapped[UUID] = mapped_column(ForeignKey("contact.id"))


class ContactTag(Base):
    __tablename__ = "contact_tag"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    tag_id: Mapped[UUID] = mapped_column(ForeignKey("tag.id"))
    contact_id: Mapped[UUID] = mapped_column(ForeignKey("contact.id"))
