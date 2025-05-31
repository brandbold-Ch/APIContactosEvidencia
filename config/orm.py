from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker, SessionTransaction
from models.models import *

engine = create_engine("postgresql://contacts_cvlb_user:gMqXglwUcdhy5HPc7770cl1Vca9Yxj4y@dpg-d0t7b6be5dus73fj79l0-a/contacts_cvlb", echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, class_=Session)
Base.metadata.create_all(engine)


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
