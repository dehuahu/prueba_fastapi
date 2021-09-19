from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


# Create SQLAlchemy models from the Base class
# We will use this Base class we created before to create the SQLAlchemy models.
# SQLAlchemy uses the term "model" to refer to these classes and instances that interact with the database.

# But Pydantic also uses the term "model" to refer to something different, the data validation, conversion, and documentation classes and instances.

# The __tablename__ attribute tells SQLAlchemy the name of the table to use in the database for each of these models.

# Dentro de la clase estan los atributos id, title, body. Cada atributo corresponde a una columna de la tabla de la bd.
# We use Column from SQLAlchemy as the default value.
# And we pass a SQLAlchemy class "type", as Integer, String, and Boolean, that defines the type in the database, as an argument.
class Blog(Base):
    __tablename__= "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
