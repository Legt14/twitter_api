from datetime import date
from typing import Optional

from pydantic import BaseModel


class BaseTweet(BaseModel):
    date = date.today()
    like: int
    comment: int
    retweet: int


class CreateTweet(BaseTweet):
    content: str


class Tweet(CreateTweet):
    id: int

    class Config:
        orm_mode = True
