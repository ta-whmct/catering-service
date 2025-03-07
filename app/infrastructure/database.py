# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.settings import database_uri

engine = create_engine(database_uri, echo=True)


def generate_session() -> Session:
    return sessionmaker(bind=engine)()
