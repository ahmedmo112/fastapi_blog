from fastapi import  FastAPI 
from blog import  models 
from blog.database import engine
from blog.routers import blog, user ,authentiction



app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentiction.router)
app.include_router(blog.router)
app.include_router(user.router)














# @app.post('/blog', status_code=status.HTTP_201_CREATED,tags=['blogs'])
# def create(request: schemas.Blog, db :Session = Depends(get_db)):
#     new_blog = models.Blog(
#         title = request.title,
#         body = request.body,
#         user_id = 1
#     )
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog
    

# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs']) # response_model=List[schemas.ShowBlog] it will get just the title of blogs
# def all(db :Session = Depends(get_db)):                 # as we do that at schemas.py so we can costomize it
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/blog/{id}', status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])
# def show(id,response: Response,db :Session = Depends(get_db), ):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not avaialable")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': f"Blog with the id {id} is not avaialable"}
    
#     return blog


# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
# def destroy(id,response: Response,db :Session = Depends(get_db),):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')

#     blog.delete(synchronize_session=False)

#     db.commit()

#     return {'detail': f'blog with id {id} has been deleted'}


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])    
# def update(id,request: schemas.Blog ,db :Session = Depends(get_db)):
#     update_blog = models.Blog(
#         title = request.title,
#         body = request.body
#     )
#     blog= db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')

#     blog.update({'title':request.title,'body':request.body},synchronize_session=False)

#     db.commit() 

#     return {'detail':"updated"}






# @app.post('/user', response_model=schemas.ShowUser,tags=['users'])
# def create_user(request: schemas.User,db :Session = Depends(get_db)):
#     hashedPassword = Hash.bycrpt(request.password)
#     new_user = models.User(
#         name = request.name,
#         email = request.email,
#         password = hashedPassword
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
# def get_user(id: int, db :Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with id {id} not found')
    
#     return user

