from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import Calificaciones
from schemas.schemas import Calificacion

calif = APIRouter(
    prefix="/calificaciones",
    tags=["calificaciones"]
    # responses={404: {"description": "Not found"}}
)

@calif.post("/", response_model=Calificacion)
def create_calificacion(c: Calificacion, db: Session = Depends(get_db)) -> Calificacion:
    db_calificacion = db.query(Calificaciones).filter(Calificaciones.id_calificacion == c.id_calificacion).first()
    if db_calificacion:
        raise HTTPException(status_code=400, detail="Calificacion already registered")
    new_calificacion = Calificaciones(
        calificacion=c.calificacion,
        id_alumno=c.id_alumno,
        id_materia=c.id_materia
    )
    db.add(new_calificacion)
    db.commit()
    db.refresh(new_calificacion)
    return new_calificacion

@calif.get("/", response_model=list[Calificacion])
def read_calificacions(db: Session = Depends(get_db)) -> list[Calificacion]:
    return db.query(Calificaciones).all()

@calif.get("/{id_calificacion}", response_model=Calificacion)
def read_calificacion(id_calificacion: int, db: Session = Depends(get_db)) -> Calificacion:
    db_calificacion = db.query(Calificaciones).filter(Calificaciones.id_calificacion == id_calificacion).first()
    if db_calificacion is None:
        raise HTTPException(status_code=404, detail="Calificacion not found")
    return db_calificacion

@calif.put("/{id_calificacion}", response_model=Calificacion)
def update_calificacion(id_calificacion:int, c:Calificacion, db: Session = Depends(get_db)) -> Calificacion:
    db_calificacion = db.query(Calificaciones).filter(Calificaciones.id_calificacion == id_calificacion).first()
    db_calificacion.calificacion=c.calificacion
    db_calificacion.id_alumno=c.id_alumno
    db_calificacion.id_materia=c.id_materia
    db.commit()
    return db_calificacion

@calif.delete("/{id_calificacion}")
def delete_calificacion(id_calificacion:int, db: Session = Depends(get_db)):
    try:
        db.query(Calificaciones).filter(Calificaciones.id_calificacion == id_calificacion).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"Delete success": id_calificacion}