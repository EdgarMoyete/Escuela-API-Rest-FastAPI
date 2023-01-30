from fastapi import APIRouter, Depends, Response, status, HTTPException
# from typing import Any
# from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import especialidad
from schemas.especialidades import Especialidad

espec = APIRouter()

def get_especialidades(db: Session, skip: int = 0, limit: int = 100):
    return db.query(especialidad).offset(skip).limit(limit).all()

def get_especialidad(db: Session, id_especialidad: int):
    return db.query(especialidad).filter(especialidad.id_especialidad == id_especialidad).first()

def create_new_especialidad(db: Session, e: Especialidad):
    db_especialidad = especialidad(
        especialidad=e.especialidad,
        id_carrera=e.id_carrera
    )
    db.add(db_especialidad)
    db.commit()
    db.refresh(db_especialidad)
    return db_especialidad

@espec.get("/especialidades/", response_model=list[Especialidad], tags=["especialidades"])
def read_especialidades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[Especialidad]:
    return get_especialidades(db, skip=skip, limit=limit)

@espec.get("/especialidades/{id_especialidad}", response_model=Especialidad)
def read_especialidad(id_especialidad: int, db: Session = Depends(get_db)):
    db_especialidad = get_especialidad(db, id_especialidad=id_especialidad)
    if db_especialidad is None:
        raise HTTPException(status_code=404, detail="Especialidad not found")
    return db_especialidad

@espec.post("/especialidades/", response_model=Especialidad)
def create_especialidad(e: Especialidad, db: Session = Depends(get_db)):
    db_especialidad = get_especialidad(db, id_especialidad=e.id_especialidad)
    if db_especialidad:
        raise HTTPException(status_code=400, detail="Especialidad already registered")
    return create_new_especialidad(db=db, e=e)