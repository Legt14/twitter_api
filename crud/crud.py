from cryptography.fernet import Fernet
from datetime import date

from sqlalchemy.orm import Session
from model import models
from schema import users, tweet


key = Fernet.generate_key()
fernet = Fernet(key)


# USERS
def create_user(
        db: Session,
        user: users.CreateUser):
    password_encryp = fernet.encrypt(user.password.encode('utf-8'))
    db_user = models.Users(
        name=user.name,
        lastname=user.lastname,
        user_name=user.user_name,
        description=user.description,
        age=user.age,
        email=user.email,
        password=password_encryp,)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(
        db: Session,
        user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def create_tweet(db: Session,
                 make_tweet: tweet.CreateTweet,
                 usr_id: int):
    db_tweet = models.Tweets(**make_tweet.dict(), user_id=usr_id)
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet


