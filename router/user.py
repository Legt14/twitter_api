from fastapi import APIRouter, status, Path
from models.user_model import users
from config.db import conn
from schema.users import BaseUser

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get(
    path='/users',
    status_code=status.HTTP_200_OK,
    tags=['Users'],
    summary='Users')
def get_user():
    return conn.execute(users.select()).fetchall()


@user.post(
    path='/users/create_user',
    status_code=status.HTTP_201_CREATED,
    tags=['Users'],
    summary='Create users'
)
def create_user(
        user: BaseUser
):
    new_user = {'name': user.name,
                'lastname': user.lastname,
                'age': user.age,
                'user_name': user.user_name,
                'email': user.email,
                "password": f.encrypt(user.password.encode('utf-8'))}
    conn.execute(users.insert().values(new_user))
    return new_user


@user.get(
    path='/users/{user_id}',
    status_code=status.HTTP_200_OK,
    tags=['Users'],
    summary='Get user'
)
def get_user(
        user_id: int = Path(...)
):
    return conn.execute(users.select().where(users.c.id == user_id)).first()


