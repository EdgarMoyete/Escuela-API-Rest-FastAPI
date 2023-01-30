from pydantic import BaseModel
from typing import Optional

class Calificacion(BaseModel):
    id_calificacion: Optional[int]
    calificacion: float
    id_alumno: str
    id_materia: str