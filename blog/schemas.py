
# Create the Pydantic models
# To avoid confusion between the SQLAlchemy models and the Pydantic models, we will have the file models.py with the SQLAlchemy models,
# and the file schemas.py with the Pydantic models.
#
# These Pydantic models define more or less a "schema" (a valid data shape).
#
# So this will help us avoiding confusion while using both

from pydantic import BaseModel #Cuando creamos una clase tenemos que importar BaseModel

# Creamos un pydantic models o schemas que se usaran cuando se lean los datos y los devuelvan desde el API.
class Blog(BaseModel): #Siempre tenemos que indicar que es un pydantic model
    title: str
    body: str