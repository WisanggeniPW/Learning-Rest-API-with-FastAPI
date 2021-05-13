from fastapi import APIRouter, FastAPI, Depends, status, Response, HTTPException
from blog import database, schemas, models
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.repository import user


router = APIRouter(
    prefix='/user',
    tags=['user']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session=Depends(get_db)):
    return user.show(id, db)