from pydantic import BaseModel
from typing import Optional

class Especialidad(BaseModel):
    id_especialidad: Optional[int]
    especialidad: str
    id_carrera: int
    
    class Config:
        orm_mode = True