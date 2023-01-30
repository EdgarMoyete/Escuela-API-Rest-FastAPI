from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import Materias
from schemas.schemas import Materia

mater = APIRouter(
    prefix="/materias",
    tags=["materias"]
    # responses={404: {"description": "Not found"}}
)

@mater.post("/", response_model=Materia)
def create_materia(m: Materia, db: Session = Depends(get_db)) -> Materia:
    db_materia = db.query(Materias).filter(Materias.id_materia == m.id_materia).first()
    if db_materia:
        raise HTTPException(status_code=400, detail="Materia already registered")
    new_materia = Materias(
        materia=m.materia,
        id_carrera=m.id_carrera
    )
    db.add(new_materia)
    db.commit()
    db.refresh(new_materia)
    return new_materia

@mater.get("/", response_model=list[Materia])
def read_materias(db: Session = Depends(get_db)) -> list[Materia]:
    return db.query(Materias).all()

@mater.get("/{id_materia}", response_model=Materia)
def read_materia(id_materia: int, db: Session = Depends(get_db)) -> Materia:
    db_materia = db.query(Materias).filter(Materias.id_materia == id_materia).first()
    if db_materia is None:
        raise HTTPException(status_code=404, detail="Materia not found")
    return db_materia

@mater.put("/{id_materia}", response_model=Materia)
def update_materia(id_materia:int, m:Materia, db: Session = Depends(get_db)) -> Materia:
    db_materia = db.query(Materias).filter(Materias.id_materia == id_materia).first()
    db_materia.materia=m.materia
    db_materia.id_carrera=m.id_carrera
    db.commit()
    return db_materia

@mater.delete("/{id_materia}")
def delete_materia(id_materia:int, db: Session = Depends(get_db)):
    try:
        db.query(Materias).filter(Materias.id_materia == id_materia).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"Delete success": id_materia}