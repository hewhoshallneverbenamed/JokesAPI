from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship

class Joke(Base):
    __tablename__ = "jokes"

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    joke_text = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    avg_rating = Column(Integer, default=0)
    num_ratings = Column(Integer, default=0)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
    category = relationship("Category")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    email = Column(String,unique=True , nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

class Rating(Base):
    __tablename__ = "ratings"

    joke_id = Column(Integer, ForeignKey("jokes.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, primary_key=True)

    rating = Column(Integer, nullable=False)
    
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

    joke = relationship("Joke")

    user = relationship("User")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    category_name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

