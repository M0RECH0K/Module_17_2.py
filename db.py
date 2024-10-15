from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///taskmanager.db', echo=True)
_sessionmaker = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass