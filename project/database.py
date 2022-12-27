from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://chinmay:Z6mTjN2HI1F8L4m4ZdiSkZR0azMa92Ui@dpg-cekoek1gp3jlcslkqfk0-a.singapore-postgres.render.com/fastapi_ire4'
engine = create_engine(SQLALCHEMY_DATABASE_URL)


sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()