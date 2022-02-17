from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import schemas , models 
# from blog.routers.authentiction import USER_ID

def get_all(db: Session):
    
    blogs = db.query(models.Blog).all()
    return blogs

    

def create(db: Session,request: schemas.Blog):
    new_blog = models.Blog(
        title = request.title,
        body = request.body,
        user_id = 1   #try to get user id 
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog) 
    return new_blog



def show(db: Session,id:int):
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not avaialable")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"Blog with the id {id} is not avaialable"}
    
    return blog



def destroy(db: Session,id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')

    blog.delete(synchronize_session=False)

    db.commit()

    return {'detail': f'blog with id {id} has been deleted'}





def update(db: Session,id:int,request: schemas.Blog):
    update_blog = models.Blog(
        title = request.title,
        body = request.body
    )
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')

    blog.update({'title':request.title,'body':request.body},synchronize_session=False)

    db.commit() 

    return {'detail':"updated"}