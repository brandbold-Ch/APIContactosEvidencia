from typing import Any, Optional, Type
from sqlalchemy import select
from sqlalchemy.orm import Session
from abstract.abstract_crud_impl import AbstractCrud, T


class BaseRepository(AbstractCrud):

    def __init__(self, model: Type[T]) -> None:
        self.model = model

    def create(
            self,
            model: T,
            session: Session,
            auto_commit: bool = True
    ) -> T:
        session.add(model)
        if auto_commit:
            session.commit()
            session.refresh(model)
        return model

    def select(
            self,
            session: Session
    ) -> list[T]:
        stmt = select(self.model)
        return list(session.execute(stmt).scalars().all())

    def get(
            self,
            _id: Any,
            session: Session
    ) -> Optional[T]:
        return session.get(self.model, _id)

    def update(
            self,
            _id: Any,
            data: dict,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        result = self.get(_id, session)
        if result:
            result.fromkeys(**data)
            session.add(result)
            if auto_commit:
                session.commit()
                session.refresh(result)
        return result

    def delete(
            self,
            _id: Any,
            session: Session,
            auto_commit: bool = True
    ) -> Optional[T]:
        result = self.get(_id, session)
        if result:
            session.delete(result)
            if auto_commit:
                session.commit()
        return result
