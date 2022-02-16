from typing import List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    id: str
    name:str
    email:str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class ShowUserwithoutBlogs(BaseModel):
    id: str
    name:str
    email:str
    

    class Config():
        orm_mode = True
class ShowBlog(BaseModel): # we use it in response_model to view the data as what we want
    title:str
    body:str
    creator: ShowUserwithoutBlogs
    class Config():
        orm_mode = True
