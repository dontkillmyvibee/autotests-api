from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, constr

NameStr = Annotated[str, constr(min_length=1, max_length=50)]


class UserSchema(BaseModel):
    """Модель данных пользователя"""
    id: UUID = Field(...)
    email: EmailStr = Field(..., min_length=1, max_length=250)
    last_name: NameStr = Field(..., alias="lastName")
    first_name: NameStr = Field(..., alias="firstName")
    middle_name: NameStr = Field(..., alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Модель запроса на создание пользователя"""
    email: EmailStr = Field(..., min_length=1, max_length=250)
    password: constr(min_length=1, max_length=250) = Field(...)
    last_name: NameStr = Field(..., alias="lastName")
    first_name: NameStr = Field(..., alias="firstName")
    middle_name: NameStr = Field(..., alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Модель ответа с данными созданного пользователя"""
    user: UserSchema = Field(...)
