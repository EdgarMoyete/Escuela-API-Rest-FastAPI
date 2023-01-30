from fastapi import APIRouter, Depends, Response, status, HTTPException
# from typing import Any
# from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import carrera
from schemas.carreras import Carrera

carre = APIRouter()

def get_carreras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(carrera).offset(skip).limit(limit).all()

def get_carrera(db: Session, id_carrera: int):
    return db.query(carrera).filter(carrera.id_carrera == id_carrera).first()

def create_new_carrera(db: Session, c: Carrera):
    db_carrera = carrera(carrera=c.carrera)
    db.add(db_carrera)
    db.commit()
    db.refresh(db_carrera)
    return db_carrera

@carre.get("/carreras/", response_model=list[Carrera], tags=["carreras"])
def read_carreras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[Carrera]:
    return get_carreras(db, skip=skip, limit=limit)

@carre.get("/carreras/{id_carrera}", response_model=Carrera)
def read_carrera(id_carrera: int, db: Session = Depends(get_db)):
    db_carrera = get_carrera(db, id_carrera=id_carrera)
    if db_carrera is None:
        raise HTTPException(status_code=404, detail="Carrera not found")
    return db_carrera

@carre.post("/carreras/", response_model=Carrera)
def create_carrera(c: Carrera, db: Session = Depends(get_db)):
    db_carrera = get_carrera(db, id_carrera=c.id_carrera)
    if db_carrera:
        raise HTTPException(status_code=400, detail="Carrera already registered")
    return create_new_carrera(db=db, c=c)