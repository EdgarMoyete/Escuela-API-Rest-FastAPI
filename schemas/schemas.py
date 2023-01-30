from pydantic import BaseModel
from typing import Optional

class Carrera(BaseModel):
    id_carrera: Optional[int]
    carrera: str

    class Config:
        orm_mode = True

class Especialidad(BaseModel):
    id_especialidad: Optional[int]
    especialidad: str
    id_carrera: int
    
    class Config:
        orm_mode = True

class Materia(BaseModel):
    id_materia: Optional[int]
    materia: str
    id_carrera: int

    class Config:
        orm_mode = True

class Alumno(BaseModel):
    id_alumno: Optional[int]
    apellido_paterno: str
    apellido_materno: str
    nombres: str
    sexo: str
    curp: str
    id_carrera: int
    id_especialidad: int

    class Config:
        orm_mode = True

class Calificacion(BaseModel):
    id_calificacion: Optional[int]
    calificacion: float
    id_alumno: int
    id_materia: int

    class Config:
        orm_mode = True