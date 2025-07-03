from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker, SessionTransaction
from models.models import *

engine = create_engine("postgresql://contacts_eg59_user:lVuak2JSKXe8Gl5EA281OrrpgtpaxFLq@dpg-d1jf8gidbo4c73c9f2o0-a/contacts_eg59", echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, class_=Session)
Base.metadata.create_all(engine)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
