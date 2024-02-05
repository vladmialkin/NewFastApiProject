import re
import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from pydantic.functional_validators import field_validator

# API модели Pydantic

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        from_attributes = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator('name', 'surname')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(status_code=422, detail="Поле должно содержать только буквы")
        return value


class DeleteUserResponse(BaseModel):
    deleted_user_id: uuid.UUID


class GetUserResponse(BaseModel):
    get_user_id: uuid.UUID


class UpdatedUserResponse(BaseModel):
    updated_user_id: uuid.UUID


class UpdateUserRequest(BaseModel):
    name: Optional[constr(min_length=1)]
    surname: Optional[constr(min_length=1)]
    email: Optional[EmailStr]

    @validator("name", pre=True)
    def validate_name(cls, value):
        if value is not None and not LETTER_MATCH_PATTERN.match(value):
            raise ValueError("Name should contain only letters")
        return value

    @validator("surname", pre=True)
    def validate_surname(cls, value):
        if value is not None and not LETTER_MATCH_PATTERN.match(value):
            raise ValueError("Surname should contain only letters")
        return value
