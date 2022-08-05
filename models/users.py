import datetime
from pydantic import BaseModel, EmailStr, validator, constr
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    hashed_password: str
    created_date: datetime.datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=7)
    password2: str

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Password do not match')
        return v
