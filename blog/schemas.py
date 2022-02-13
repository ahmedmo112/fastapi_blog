from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class ShowBlog(BaseModel): # we use it in response_model to view the data as what we want
    title:str
    body:str
    class Config():
        orm_mode = True
