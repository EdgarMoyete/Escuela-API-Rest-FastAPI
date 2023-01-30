from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import Carreras
from schemas.schemas import Carrera

carre = APIRouter(
    prefix="/carreras",
    tags=["carreras"]
    # responses={404: {"description": "Not found"}}
)

@carre.post("/", response_model=Carrera)
def create_carrera(c: Carrera, db: Session = Depends(get_db)) -> Carrera:
    db_carrera = db.query(Carreras).filter(Carreras.id_carrera == c.id_carrera).first()
    if db_carrera:
        raise HTTPException(status_code=400, detail="Carrera already registered")
    new_carrera = Carreras(carrera=c.carrera)
    db.add(new_carrera)
    db.commit()
    db.refresh(new_carrera)
    return new_carrera

@carre.get("/", response_model=list[Carrera])
def read_carreras(db: Session = Depends(get_db)) -> list[Carrera]:
    return db.query(Carreras).all()

@carre.get("/{id_carrera}", response_model=Carrera)
def read_carrera(id_carrera: int, db: Session = Depends(get_db)) -> Carrera:
    db_carrera = db.query(Carreras).filter(Carreras.id_carrera == id_carrera).first()
    if db_carrera is None:
        raise HTTPException(status_code=404, detail="Carrera not found")
    return db_carrera

@carre.put("/{id_carrera}", response_model=Carrera)
def update_carrera(id_carrera:int, c:Carrera, db: Session = Depends(get_db)) -> Carrera:
    db_carrera = db.query(Carreras).filter(Carreras.id_carrera == id_carrera).first()
    db_carrera.carrera=c.carrera
    db.commit()
    return db_carrera

@carre.delete("/{id_carrera}")
def delete_carrera(id_carrera:int, db: Session = Depends(get_db)):
    try:
        db.query(Carreras).filter(Carreras.id_carrera == id_carrera).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"Delete success": id_carrera}