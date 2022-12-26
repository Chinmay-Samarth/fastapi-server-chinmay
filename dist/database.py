from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://chinmay:pWjW2FQTip1n06kVTe3viEU0v3h9HNkL@dpg-cekmf0pa6gdkdn0dvp6g-a.singapore-postgres.render.com/fastapi_ogel'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()