import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Asegúrate de que solo exista una clase User
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name_personaje = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    especie = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)  # Añade una clave primaria
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    planeta = relationship(Planeta)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    personaje = relationship(Personaje)
    fecha_agregado = Column(String(250), nullable=False)
    
def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
