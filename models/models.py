from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .db import base

class carrera(base):
    __tablename__ = "carreras"
    id_carrera = Column(Integer, primary_key=True, index=True)
    carrera = Column(String)

class especialidad(base):
    __tablename__ = "especialidades"
    id_especialidad = Column(Integer, primary_key=True, index=True)
    especialidad = Column(String)
    id_carrera = Column(Integer, ForeignKey("carreras.id_carrera"))
    
    carrera = relationship("carrera") # back_populates=

class materia(base):
    __tablename__ = "materias"
    id_materia = Column(Integer, primary_key=True, index=True)
    materia = Column(String)
    id_carrera = Column(Integer, ForeignKey("carreras.id_carrera"))
    
    carrera = relationship("carrera") # back_populates=

class alumno(base):
    __tablename__ = "alumnos"
    id_alumno = Column(Integer, primary_key=True, index=True)
    apellido_paterno = Column(String)
    apellido_materno = Column(String)
    nombres = Column(String)
    sexo = Column(String)
    curp = Column(String)
    id_carrera = Column(Integer, ForeignKey("carreras.id_carrera"))
    id_especialidad = Column(Integer, ForeignKey("especialidades.id_especialidad"))
    
    carrera = relationship("carrera") # back_populates=
    especialidad = relationship("especialidad") # back_populates=

class calificacion(base):
    __tablename__ = "calificaciones"
    id_calificacion = Column(Integer, primary_key=True, index=True)
    calificacion = Column(Float)
    id_alumno = Column(Integer, ForeignKey("alumnos.id_alumno"))
    id_materia = Column(Integer, ForeignKey("materias.id_materia"))
    
    alumno = relationship("alumno") # back_populates=
    materia = relationship("materia") # back_populates=