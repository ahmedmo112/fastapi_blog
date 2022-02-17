from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import schemas , models 
from blog.hashing import Hash

def create(request: schemas.User,db :Session ):
    hashedPassword = Hash.bycrpt(request.password)
    new_user = models.User(
        name = request.name,
        email = request.email,
        password = hashedPassword
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def getUser(id:int,db :Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} not found')
    
    return user