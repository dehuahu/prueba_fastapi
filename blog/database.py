# DATABASE CONNECTION

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database URL for SQLAlchemy

# En esta parte introducimos la url de la base de datos en SQLite
# This is the main line that you would have to modify if you wanted to use a different database.
SQLALCHAMY_DATABASE_URL= "sqlite:///./blog.db"
# Si nuestra base de datos estuviera en postgresql:
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# Create the SQLAlchemy engine

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread":False})
# El argumento connect_args={"check_same_thread": False} solo es necesario para la base de datos SQLite,
# si usamos postgresql no necesitamos incorporar ese argumento

# Create a SessionLocal class
# Cada instancia de la clase SessionLocal será una sesión de la base de datos. La clase SessionLocal no es una sesion de la bd.
# But once we create an instance of the SessionLocal class, this instance will be the actual database session.
# We name it SessionLocal to distinguish it from the Session we are importing from SQLAlchemy.
# We will use Session (the one imported from SQLAlchemy) later.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
# Now we will use the function declarative_base() that returns a class.
# Later we will inherit from this class to create each of the database models or classes (the ORM models)
Base= declarative_base()

