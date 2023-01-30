from pydantic import BaseModel
from typing import Optional

class Materia(BaseModel):
    id_materia: Optional[int]
    materia: str
    id_carrera: int