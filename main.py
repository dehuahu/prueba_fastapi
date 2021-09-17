from fastapi import FastAPI


app= FastAPI() #Instance app
# GET/POST/DELETE/PUT métodos se les denomina la operación (operation) del path.
# El endpoint o path es lo que va entre ()
# @app es el path operation decorator
@app.get("/") #Creamos el endpoint

# La función es el path operation function, se trata de la operación que vamos a desempeñar en el path
def index(): #Aqui tenemos la pag principal
    return {"data": "blog list"}

@app.get("/about") #aqui tenemos una extensión del path
def about():
    return {"data": "about page"}

# Si quisieramos que nuestra endpoint fuese /blog/1
# Siendo el 1 el id del blog, este id puede variar. Asi que tendremos que añadirlo como parámetro
# Cuando que una ruta dinámica (dynamic routing) debemos usar {} y dentro el nombre del parámetro
# Cuando el parámetro se encuentra en el path, el full stack tendra que introducirlo en la misma ruta
# @app.get("/blog/{id}")
# # El parametro tambien tenemos que introducirlo en la función
# def show(id):
#     # fetch blog with id=id
#     return {"data": id} #Nos devuelve un string con el id

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


# Si quisieramos que nos devolviese un número tenemos que indicar el tipo de parámetro
@app.get("/blog/{id}")
# El parametro tambien tenemos que introducirlo en la función
def show(id: int): #en la función definimos el parametro como un num entero
    # fetch blog with id=id
    return {"data": id} #Nos devuelve un num entero como id
# Si no se le introduce un int sino que una string el la petición mostrará el error

@app.get("/blog/{id}/comments")
def comments(id):
    # fetch (peticiones asíncronas) comments of blog with id = id
    return {"data": {"1", "2"}}

# En este caso de los blogs no publicados nos da error, lo que pasa es que fastAPI lee el código linea por linea
# Como posteriormente hemos indicado que despues de blog va un núm entero nos genera error,
# para solucionarlo debemos cambiar el código hacia arriba para que sea la primera entrada del endpoint que
#empieza por blog
# @app.get("/blog/unpublished")
# def unpublished():
#     return {"data": "all unpublished blogs"}