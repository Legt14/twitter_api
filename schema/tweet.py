from typing import Optional
from datetime import date

from pydantic import BaseModel, Field



class BaseTweet(BaseModel):
    content: str = Field(...)
    tweet_date: str = date.today()

class CreateTweet(BaseTweet):
    pass


class Tweet(BaseTweet):
    like_count: int
    comment_count: int
    retweet_count: int

    class Config:
        orm_mode = True
