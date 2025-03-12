from typing import List
from pydantic import BaseModel, Field, field_validator

class UserPreferences(BaseModel):
    timezone: str

class User(BaseModel):
    username: str = Field(..., min_length=1, description="Username cannot be empty")
    password: str = Field(..., min_length=1, description="Password cannot be empty")
    roles: List[str]
    preferences: UserPreferences
    created_ts: float
    active: bool = True

    @field_validator('username', 'password')
    def check_empty_fields(cls, value):
        if not value.strip():
            raise ValueError('Field cannot be empty')
        return value