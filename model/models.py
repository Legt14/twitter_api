from sqlalchemy import Column, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    lastname = Column(String(20))
    age = Column(Integer)
    user_name = Column(String(20))
    email = Column(String(250))
    is_verified = Column(Boolean)
    password = Column(String(250))
    description = Column(String(250))
    tweet_id = relationship('Tweets', back_populates='user')


class Tweets(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    content = Column(String(256))
    like = Column(Integer)
    comment = Column(Integer)
    retweet = Column(Integer)
    date = Column(Date)

    user_id = Column(ForeignKey('users.id'))
    user = relationship('Users', back_populates='tweet_id')

