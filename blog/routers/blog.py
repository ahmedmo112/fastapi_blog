from typing import List
from .. import schemas 
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response,status
from ..repository import blogRepo

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)



@router.get('/',response_model=List[schemas.ShowBlog],) # response_model=List[schemas.ShowBlog] it will get just the title of blogs
def all(db :Session = Depends(get_db)):                 # as we do that at schemas.py so we can costomize it
    return blogRepo.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db :Session = Depends(get_db)):
    return blogRepo.create(db,request)


@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog,)
def show(id,db :Session = Depends(get_db), ):
    return blogRepo.show(db=db,id=id)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,)
def destroy(id,response: Response,db :Session = Depends(get_db),):
    return blogRepo.destroy(db=db,id=id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED,)    
def update(id,request: schemas.Blog ,db :Session = Depends(get_db)):
    return blogRepo.update(id=id,request=request,db=db)
