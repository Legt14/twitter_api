from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from crud import crud
from model import models
from schema import users, tweet

from config.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    path='/create_user',
    status_code=status.HTTP_201_CREATED,
    summary='Create user',
    tags=['Users'],
    response_model=users.User)
def create_user(
        user: users.CreateUser,
        db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email is already registered')

    return crud.create_user(db, user)


@router.get(
    path='/users/{user_id}',
    status_code=status.HTTP_200_OK,
    summary='Get user',
    tags=['Users'],
    response_model=users.User
)
def get_user(user_id,  db: Session = Depends(get_db)):
    usr = crud.get_user(db, user_id)
    if not usr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not exist')
    return usr


@router.get(
    path='/users',
    status_code=status.HTTP_200_OK,
    summary='Get users',
    tags=['Users'],
    response_model=list[users.User]
)
def get_users(db: Session = Depends(get_db), skip=0, limit=100):
    usr = crud.get_users(db, skip=skip, limit=limit)
    return usr


@router.post(
    path='/users/{user_id}/create_tweet',
    status_code=status.HTTP_201_CREATED,
    summary='POST Tweets',
    tags=['Tweets'],
    #response_model=tweet.Tweet
)
def create_tweet(
        user_id: int,
        make_tweet: tweet.CreateTweet,
        db: Session = Depends(get_db)):

    return crud.create_tweet(db=db, make_tweet=make_tweet, usr_id=user_id)

