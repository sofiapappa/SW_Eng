from pydantic import BaseModel, Field
from typing import List


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The Username",
        description="whatever...",
        min_length=1,
        default=None
    )
    liked_posts: List[int] = Field(
        description="Array of ids the user liked",
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


class MultipleUserResponse(BaseModel):
    users: List[FullUserProfile]
    total: int


class CreateUserResponse(BaseModel):
    user_id: int
