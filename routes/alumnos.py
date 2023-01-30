from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.db import get_db
from models.models import Alumnos
from schemas.schemas import Alumno

alumn = APIRouter(
    prefix="/alumnos",
    tags=["alumnos"]
    # responses={404: {"description": "Not found"}}
)

@alumn.post("/", response_model=Alumno)
def create_alumno(a: Alumno, db: Session = Depends(get_db)) -> Alumno:
    db_alumno = db.query(Alumnos).filter(Alumnos.id_alumno == a.id_alumno).first()
    if db_alumno:
        raise HTTPException(status_code=400, detail="Alumno already registered")
    new_alumno = Alumnos(
        apellido_paterno=a.apellido_paterno,
        apellido_materno=a.apellido_materno,
        nombres=a.nombres,
        sexo=a.sexo,
        curp=a.curp,
        id_carrera=a.id_carrera,
        id_especialidad=a.id_especialidad
    )
    db.add(new_alumno)
    db.commit()
    db.refresh(new_alumno)
    return new_alumno

@alumn.get("/", response_model=list[Alumno])
def read_alumnos(db: Session = Depends(get_db)) -> list[Alumno]:
    return db.query(Alumnos).all()

@alumn.get("/{id_alumno}", response_model=Alumno)
def read_alumno(id_alumno: int, db: Session = Depends(get_db)) -> Alumno:
    db_alumno = db.query(Alumnos).filter(Alumnos.id_alumno == id_alumno).first()
    if db_alumno is None:
        raise HTTPException(status_code=404, detail="Alumno not found")
    return db_alumno

@alumn.put("/{id_alumno}", response_model=Alumno)
def update_alumno(id_alumno:int, a:Alumno, db: Session = Depends(get_db)) -> Alumno:
    db_alumno = db.query(Alumnos).filter(Alumnos.id_alumno == id_alumno).first()
    db_alumno.apellido_paterno=a.apellido_paterno
    db_alumno.apellido_materno=a.apellido_materno
    db_alumno.nombres=a.nombres
    db_alumno.sexo=a.sexo
    db_alumno.curp=a.curp
    db_alumno.id_carrera=a.id_carrera
    db_alumno.id_especialidad=a.id_especialidad
    db.commit()
    return db_alumno

@alumn.delete("/{id_alumno}")
def delete_alumno(id_alumno:int, db: Session = Depends(get_db)):
    try:
        db.query(Alumnos).filter(Alumnos.id_alumno == id_alumno).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {"Delete success": id_alumno}