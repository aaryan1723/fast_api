from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from typing import Annotated
import models as models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
#from Fastapi.security import OAuth2PasswordBearer , OAuthPasswordRequestForm




app = FastAPI()
models.base.metadata.create_all(bind=engine)

class Post_Base(BaseModel):
    title: str
    content: str
    user_id: int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/post/", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post_Base, db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    return db_post

@app.delete("/post/{post_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail='Post was not found')
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}

@app.delete("/user/{user_id}", status_code=status.HTTP_202_ACCEPTED )
async def delete_user(user_id: int, db: db_dependency):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail= 'User was not found')
    db.delete(db_user)
    db.commit()
    return {"message": "User deleated successfully"}
        

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
