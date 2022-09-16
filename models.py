from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from enum import Enum
from typing import Optional, List 

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

class userUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]