from fastapi import APIRouter# , Response, status# , HTTPException
from typing import Any
# from starlette.status import HTTP_204_NO_CONTENT

from models.db import conexion
from models.carreras import carreras
from schemas.carreras import Carrera

carre = APIRouter()

@carre.get("/carreras", response_model=list[Carrera], tags=["carreras"])
async def read() -> list[Carrera]: # REVISAR
    return conexion.execute(carreras.select()).fetchall()