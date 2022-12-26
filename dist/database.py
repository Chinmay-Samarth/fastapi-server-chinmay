from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./user.db?mode=rw'

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True, connect_args={'check_same_thread': False})
engine.connect()

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()