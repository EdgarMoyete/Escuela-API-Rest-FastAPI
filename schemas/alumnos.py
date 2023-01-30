from pydantic import BaseModel
from typing import Optional

class Alumno(BaseModel):
    id_alumno: Optional[int]
    apellido_paterno: str
    apellido_materno: str
    nombres: str
    sexo: str
    curp: str
    id_carrera: int
    id_especialidad: int