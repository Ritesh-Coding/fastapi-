from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app= FastAPI()

@app.get('/')
def index():
    return {"data": "blog list"}

@app.get("/blog/unpublished")   #keep these at the first in order that it does not conflict with the lower one  
def unpublished():
    return {"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id : int):
    return {"specific blog havind id ": id}

@app.get("/blog")
def show(limit : int =10,published : bool=True,sort:Optional[str]=None):  #we can also give the optional value here and the third parameter is optional 
    if published:
         return {"specific blog havind id ": limit}
    else:
        return {"data":"No published blog"}
    

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]
    
    
#learning post modal
@app.post("/blog")
def create_blog(request: Blog):
    return {"data":f"Blog is created with {request.title} having {request.body} and pusblised as {request.published}"}
   
   
# if __name__ == "__main__":  #if we want to change the port  
#     uvicorn.run(app,host="127.0.0.1",port= '9000') 