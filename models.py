from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field, EmailStr


_date = datetime.date


class BaseUsers(BaseModel):
    first_name: str = Field(..., max_length=15, min_length=1)
    last_name: str = Field(..., max_length=15, min_length=1)
    age: int = Field(...)
    user_name: str = Field(..., max_length=10, min_length=5)
    email: EmailStr = Field(...)
    mobile: Optional[str] = Field(..., min_length=10, max_length=10)

    class Config:
        schema_extra = {
            'example':{
                'first_name': 'Leandro',
                'last_name': 'Gomez',
                'age': 20,
                'email': 'email@example.com',
                'mobile': '+00-0000000'
            }
        }



class User(BaseUsers):
    password: str = Field(..., min_length=8)


class UserOut(BaseUsers):
    first_name: str
    user_name: str
    is_verifict: bool = Field(default=None)
    user_id: int = Field(...)
    
    class Config:
        schema_extra = {
            'example':{
                'first_name': 'first_name',
                'user_name': 'user_name',
                'is_verifict': False,
                'user_id': 1
            }
        }


class BaseTweets(BaseModel):
    tweet_id: int = Field(...)
    users: str = Field()
    content: str = Field(..., max_length=250, min_length=1)
   
    
    class Config:
        schema_extra = {
            'example':{
                'tweet_id': 1,
                'users': "UserOut",
                'content': 'Cupidatat est mollit reprehenderit culpa.',
            }
        }


class Tweets(BaseTweets):
    pass

class TweetDetail(BaseTweets):
    pass



class Interactions(BaseTweets):
    is_edited: bool = Field(default=False)
    comment_count: Optional[int] = Field(default=None) 
    like_count: Optional[int] = Field(default=0)
    retweet_count: Optional[int] = Field(default=0)
    
    class Config:
        schema_extra = {
            'example':{
                'comment_count': 0,
                'like_count': 0,
                'retweet_count': 0
            }
        }

class InteractionsDetail(Interactions):
    comment: Optional[str] = Field(default=None)
    
    class Config:
        schema_extra = {
            'example':{
                'comment': 'Ex non id dolor exercitation est commodo ea consequat tempor.'
            }
        }