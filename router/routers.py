from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from crud import crud
from model import models
from schema import users

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

    # db_user = crud.create_user(db, email=user.email)

    # if db_user:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User is already registered')
    
    return crud.create_user(db, user)


# @router.get(
#     path='/users',
# )