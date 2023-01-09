import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    correo = Column(String(250), nullable=False)
    clave = Column(String(250), nullable=False)
    fecha_suscripcion = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    edad = Column(Integer, nullable=False)
    nacimiento = Column(String(250), nullable=False)
    altura = Column(Integer, nullable=False)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    diametro = Column(Integer, nullable=False)
    terreno = Column(String(250), nullable=False)
    poblacion = Column(Integer, nullable=False)

class Likes_Personajes(Base):
    __tablename__ = 'likes_personajes'
    usuario_id = Column(Integer, ForeignKey('usuario.id') , primary_key=True, nullable=False)
    personajes_id = Column(Integer,  ForeignKey('personajes.id'), primary_key=True, nullable=False)
    
class Likes_Planetas(Base):
    __tablename__ = 'likes_planetas'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True, nullable=False )
    planetas_id = Column(Integer, ForeignKey('planetas.id'), primary_key=True, nullable=False )



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
