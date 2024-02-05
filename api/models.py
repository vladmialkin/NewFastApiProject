import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from pydantic.functional_validators import field_validator

# API модели Pydantic

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


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
