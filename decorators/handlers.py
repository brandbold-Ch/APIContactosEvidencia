from functools import wraps
from typing import Callable
from psycopg2 import IntegrityError, OperationalError
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from exceptions.exceptions import *


def rollback(session: Session) -> None:
    if (session and session.is_active and
            is_persistent_operation(session)):
        session.rollback()


def is_persistent_operation(session: Session) -> bool:
    return bool(session.new or
                session.dirty or
                session.deleted)


def some_session(*args) -> Optional[Session]:
    for arg in args:
        if isinstance(arg, Session):
            return arg
    return None


def exception_handler(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = some_session(*args)

        try:
            return func(*args, **kwargs)

        except IntegrityError as e:
            rollback(session)
            raise BadRequest("Violación de integridad de datos", data={"detail": str(e.orig)})

        except NoResultFound:
            rollback(session)
            raise NotFound("No se encontró el recurso solicitado")

        except UnmappedInstanceError:
            rollback(session)
            raise BadRequest("Instancia no mapeada por SQLAlchemy")

        except OperationalError as e:
            rollback(session)
            raise InternalServerError("Error operacional en la base de datos", data={"detail": str(e.orig)})

        except SQLAlchemyError as e:
            rollback(session)
            raise InternalServerError("Error inesperado con SQLAlchemy", data={"detail": str(e)})

        except BaseHTTPException:
            raise

        except Exception as e:
            rollback(session)
            raise InternalServerError("Error inesperado del sistema", data={"detail": str(e)})

    return wrapper
