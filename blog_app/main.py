from fastapi import FastAPI,Depends,status,Response,HTTPException
import uvicorn
from sqlalchemy.orm import Session
from . import schemas
from . import models
from .database import engine,get_db
app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog',status_code=201)
def create(request : schemas.Blog, db : Session = Depends(get_db)):  #Depends helps to convert the session into the pydentic thing  
    new_blog = models.Blog(title=request.title,body=request.body)
    print(new_blog)
    db.add(new_blog)
    db.commit()
    print("again ",new_blog)
    return new_blog

@app.get("/blog",status_code=status.HTTP_200_OK)
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

#in order to get the specific blog 
@app.get("/blog/{id}",status_code=400)
def show(id,response : Response,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        # return f"{id} blog is not found"
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details="Not Found")
    return blog
    
    
    
# if __name__ == "__main__":  #if we want to change the port  
#     uvicorn.run(app,host="127.0.0.1",port= '9000') 