from typing import List, Optional


from pydantic import BaseModel, Field, EmailStr

from .tweet import Tweet

class BaseUser(BaseModel):
    email: EmailStr
    name: str 
    lastname: str
    age: Optional[int]
    user_name: str
    description: Optional[str]


class CreateUser(BaseUser):
    password: str

class User(BaseUser):
    id: int
    is_verified: Optional[bool]
    tweets: List[Tweet] = []
    
    
    class Config:
        orm_mode = True
