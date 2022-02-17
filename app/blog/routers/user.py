
from blog import schemas 
from blog.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from blog.repository import userRepo

router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.post('/', response_model=schemas.ShowUser,)
def create_user(request: schemas.User,db :Session = Depends(get_db)):
    return userRepo.create(request=request,db=db)

@router.get('/{id}',response_model=schemas.ShowUser,)
def get_user(id: int, db :Session = Depends(get_db)):
    return userRepo.getUser(id,db)
