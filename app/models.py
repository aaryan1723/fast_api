from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, index=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    is_active: bool = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, index=True, nullable=False)
    description: str = Column(String)
    owner_id: int = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
