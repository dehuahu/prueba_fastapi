from fastapi import FastAPI, Depends
from . import schemas #Aqui tenemos que importar la clase, el pydantic model
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List


app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog=models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# A partir de aqui queremos almacenar lo que obtenemos del request body.
# Para ello hay que conectarse al database