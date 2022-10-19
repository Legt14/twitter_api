from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMYS_DB_URL = 'postgresql+psycopg2://postgres:admin@localhost:5432/twitter_api'

'''
THE ARGUMENT:
    connect_args={"check_same_thread": False}
    IS NEEDED ONLY IN SQLITE

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
'''

engine = create_engine(SQLALCHEMYS_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
