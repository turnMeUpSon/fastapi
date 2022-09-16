from enum import Enum
from typing import List
from typing import Optional
from uuid import UUID
from uuid import uuid4

from pydantic import BaseModel
from pydantic import Field


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'


class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]


class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]
