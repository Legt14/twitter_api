from cryptography.fernet import Fernet

from sqlalchemy.orm import Session
from model import models
from schema import users, tweet

key = Fernet.generate_key()
fernet = Fernet(key)


#USERS
def create_user(
    db: Session,
    user: users.CreateUser,):

    password_encryp = fernet.encrypt(user.password.encode('utf-8'))
    db_user = models.Users(
        name=user.name,
        lastname=user.lastname,
        user_name=user.user_name,
        description=user.description,
        age= user.age,
        email=user.email,
        password=password_encryp)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(
    db: Session,
    user_id: int):

    return db.query(models.Users).Filter(models.Users.id == user_id).first()



