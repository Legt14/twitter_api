from datetime import datetime, date
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class BaseUser(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str = Field(...)
    lastname: str = Field(...)
    age: Optional[int] = Field(default=0)
    user_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)
