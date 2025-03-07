# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import database_uri

engine = create_engine(database_uri, echo=True)


session_maker = sessionmaker(bind=engine)
