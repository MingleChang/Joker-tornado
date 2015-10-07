#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, String, Integer, SmallInteger, Date, DateTime, TIMESTAMP, Table, create_engine
from sqlalchemy import ForeignKey
# from sqlalchemy.orm import scoped_session,sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

def init_db(engine):
    Base.metadata.create_all(bind=engine)

def update_db(engine):
    pass
    
def drop_db(engine):
    Base.metadata.drop_all(bind=engine)

class User(Base):
    __tablename__ = 'user'

    userid = Column(String(50), primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    image = Column(String(200))
    realname = Column(String(50))
    nickname = Column(String(50))
    email = Column(String(200))
    telephone = Column(String(20))
    address = Column(Text)
    sex = Column(Integer)
    birthday = Column(Date)
    blood = Column(Integer)
    summary = Column(Text)

    create = Column(DateTime,default=datetime.datetime.utcnow())
    update = Column(DateTime,default=datetime.datetime.utcnow())
    
class Joke(Base):
    __tablename__='joke'

    jokeid=Column(String(50), primary_key=True)
    title=Column(String(200))
    content=Column(Text)
    status=Column(Integer,default=0)
    userid=Column(String(50), ForeignKey('user.userid'))
    tagid=Column(String(50), ForeignKey('tag.tagid'))
    create=Column(DateTime,default=datetime.datetime.utcnow())
    
class Tag(Base):
    __tablename__='tag'

    tagid=Column(String(50), primary_key=True)
    content=Column(String(50),unique=True)

class Comment(Base):
    __tablename__='comment'

    commentid=Column(String(50), primary_key=True)
    content=Column(Text)
    userid=Column(String(50), ForeignKey('user.userid'))
    jokeid=Column(String(50), ForeignKey('joke.jokeid'))
    create=Column(DateTime,default=datetime.datetime.utcnow())