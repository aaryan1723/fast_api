from database import base
from sqlalchemy import Column,Integer, String

class User(base):
    __tablename__='users'

    id=Column(Integer,primary_key=True , index=True)
    username=Column(String(50),unique=True)
    hashed_passwors = Column(String)

class Post(base):
    __tablename__='posts'

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50))
    content=Column(String(100))
    user_id=Column(Integer)