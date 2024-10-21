from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    password: str
class UserCreate(UserBase):
    pass
class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
class UserLogin(UserBase):
    pass

class JokeBase(BaseModel):
    joke_text: str
    category_id: Optional[int] = None
class JokeCreate(JokeBase):
    avg_rating: int = 0
    num_ratings: int = 0
    pass
class JokeUpdate(JokeBase):
    pass
class Joke(JokeBase):
    id: int
    # owner_id: int
    avg_rating: int
    created_at: datetime
    updated_at: datetime

    owner: User

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    id: Optional[int] = None

class CategoryBase(BaseModel):
    category_name: str
class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RatingBase(BaseModel):
    joke_id: int
    rating: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


