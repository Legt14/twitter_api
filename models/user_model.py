from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


users = Table('users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              Column('lastname', String(20)),
              Column('age', Integer),
              Column('password', String(250)),
              Column('user_name', String(20)),
              Column('email', String(255)))

meta.create_all(engine)
