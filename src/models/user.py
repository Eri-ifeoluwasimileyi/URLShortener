from pydantic import BaseModel, EmailStr, field_validator

from src.utils.validators import name_pattern


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator('username', mode='after')
    @classmethod
    def validate_name(cls, value):
        if name_pattern.match(value) is None:
            raise ValueError(f'invalid name: {value}')
        return value

    @field_validator('email', mode='after')
    @classmethod
    def validate_email(cls, value):
        if len(value) < 10:
            raise ValueError(f'invalid email: {value}')
        return value

    @field_validator('password', mode='after')
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError(f'invalid password: {value}')
        return value



class LoginUser(BaseModel):
    username: str
    email: EmailStr
    password: str
