from sqlalchemy import String, Integer,Column, Date
from database import base


class User(base):
    __tablename__ = 'user'

    username = Column(String, primary_key= True)
    password = Column(Integer)
    rank = Column(Integer)


class web_of_100(base):
    __tablename__ = 'person'
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String)
    phone = Column(Integer)
    amount = Column(Integer)


class web_amount(base):
    __tablename__ = 'amount'
    
    transaction_id = Column(Integer, primary_key=True, index=True)
    id = Column(Integer)
    submit_date = Column(Date)
