from abc import ABC, abstractmethod
from typing import TypeVar, Any, Optional
from sqlalchemy.orm import DeclarativeBase, Session

T = TypeVar("T", bound=DeclarativeBase)


class AbstractCrud(ABC):

    @abstractmethod
    def create(
            self,
            model: T,
            session: Session,
            auto_commit: bool = True
    ) -> T:
        pass

    @abstractmethod
    def select(
            self,
            session: Session
    ) -> list[T]:
        pass

    @abstractmethod
    def get(
            self,
            _id: Any,
            session: Session
    ) -> Optional[T]:
        pass

    @abstractmethod
    def update(
            self,
            _id: Any,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        pass

    @abstractmethod
    def delete(
            self,
            _id: Any,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        pass
