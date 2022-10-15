from datetime import datetime, date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class BaseUsers(BaseModel):
    email: EmailStr = Field(...)
    user_id: UUID = Field(...)

    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'email': 'example@email.com',
    #             'user_id': 'user_id'
    #         }
    #     }


class UserLogin(BaseUsers):
    password: str = Field(..., min_length=8)


class User(BaseUsers):
    user_name: str = Field(..., max_length=10, min_length=5)
    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'user_name': '@example'
    #         }
    #     }


class UserProfile(User):
    first_name: str = Field(..., max_length=15, min_length=1)
    last_name: str = Field(..., max_length=15, min_length=1)
    age: int = Field(...)
    is_verificated: bool = Field(default=None)
    mobile: Optional[str] = Field(..., min_length=10, max_length=10)
    birth_date: Optional[date] = Field(default=None)

    # class Config:
    #     schema_extra = {
    #         'example':{
    #             'first_name': 'Leandro',
    #             'last_name': 'Gomez',
    #             'age': 20,
    #             'is_verificated': False,
    #             'mobile': '+00-0000000',
    #             'brith_date': 'date'
    #         }
    #     }


class Register(UserProfile, UserLogin):
    pass


class BaseTweets(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., max_length=250, min_length=1)
    create_date: datetime = Field(default=datetime.now())
    update_date: Optional[datetime] = Field(default=None)
    by: User = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'tweet_id': 1,
                'by': "dasd",
                'content': 'Cupidatat est mollit reprehenderit culpa.',
            }
        }


class TweetsReactions(BaseTweets):
    comment_count: int = Field(...) 
    like_count: int = Field(...)
    retweet_count: int = Field(...)
    
    class Config:
        schema_extra = {
            'example': {
                'comment_count': 0,
                'like_count': 0,
                'retweet_count': 0
            }
        }


class TweetDetail(BaseTweets):
    comments: Optional[str] = Field(default=None)
    
    class Config:
        schema_extra = {
            'example': {
                'by': '@Example',
                'comments': 'Ex non id dolor exercitation est commodo ea consequat tempor.'
            }
        }


    