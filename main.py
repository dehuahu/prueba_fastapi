from fastapi import FastAPI


app= FastAPI() #Instance app

@app.get("/") #Creamos el endpoint

def index(): #Aqui tenemos la pag principal
    return {"data": {"name": "Dehua"}}

@app.get("/about") #aqui tenemos una extensión del path
def about():
    return {"data": "about page"}