from pydantic import BaseModel
from typing import Optional

class Carrera(BaseModel):
    id_carrera: Optional[int]
    carrera: str