from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///amity_db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    person_id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    role = Column(String(50))
    office = Column(String(50))
    living = Column(String(50))
    unallocated = Column(String(50))

class Rooms(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer(), primary_key=True)
    room_name = Column(String(50))
    category = Column(String(50))
