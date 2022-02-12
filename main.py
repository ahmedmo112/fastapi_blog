from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool =True,sort : Optional[str] = None):
    if published: # for query ex: /blog?limit=10
        return {'data':f"{limit} published blogs from List "}
    else:
        return {'data':f"{limit} all blogs from List "}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'All unpublished blog'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published_At: Optional[bool]    

@app.post('/blog')
def create_blog(request: Blog):
    
    return {'data': f'Blog is created with title as {request.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.2.2",port=5050)