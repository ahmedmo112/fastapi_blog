from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from blog import models
from blog import schemas ,models
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.hashing import Hash
from blog.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token




router = APIRouter(
    tags=['Authentiction']
) 

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(),db : Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid Creadentials')
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect password')

    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
   
    access_token = create_access_token(
        data={"sub": user.email},
        # expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"} 