from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker, SessionTransaction
from models.models import *

engine = create_engine("postgresql://postgres:mypostgres@localhost:5432/postgres", echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, class_=Session)
Base.metadata.create_all(engine)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
