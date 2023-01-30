from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import Especialidades
from schemas.schemas import Especialidad

espec = APIRouter(
    prefix="/especialidades",
    tags=["especialidades"]
    # responses={404: {"description": "Not found"}}
)

@espec.post("/", response_model=Especialidad)
def create_especialidad(e: Especialidad, db: Session = Depends(get_db)) -> Especialidad:
    db_especialidad = db.query(Especialidades).filter(Especialidades.id_especialidad == e.id_especialidad).first()
    if db_especialidad:
        raise HTTPException(status_code=400, detail="Especialidad already registered")
    new_especialidad = Especialidades(
        especialidad=e.especialidad,
        id_carrera=e.id_carrera
    )
    db.add(new_especialidad)
    db.commit()
    db.refresh(new_especialidad)
    return new_especialidad

@espec.get("/", response_model=list[Especialidad])
def read_especialidads(db: Session = Depends(get_db)) -> list[Especialidad]:
    return db.query(Especialidades).all()

@espec.get("/{id_especialidad}", response_model=Especialidad)
def read_especialidad(id_especialidad: int, db: Session = Depends(get_db)) -> Especialidad:
    db_especialidad = db.query(Especialidades).filter(Especialidades.id_especialidad == id_especialidad).first()
    if db_especialidad is None:
        raise HTTPException(status_code=404, detail="Especialidad not found")
    return db_especialidad

@espec.put("/{id_especialidad}", response_model=Especialidad)
def update_especialidad(id_especialidad:int, e:Especialidad, db: Session = Depends(get_db)) -> Especialidad:
    db_especialidad = db.query(Especialidades).filter(Especialidades.id_especialidad == id_especialidad).first()
    db_especialidad.especialidad=e.especialidad
    db_especialidad.id_carrera=e.id_carrera
    db.commit()
    return db_especialidad

@espec.delete("/{id_especialidad}")
def delete_especialidad(id_especialidad:int, db: Session = Depends(get_db)):
   try:
      db.query(Especialidades).filter(Especialidades.id_especialidad == id_especialidad).delete()
      db.commit()
   except Exception as e:
      raise Exception(e)
   return {"Delete success": id_especialidad}