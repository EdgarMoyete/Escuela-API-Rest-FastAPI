from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from .db import meta, engine

carreras = Table(
    "carreras",
    meta,
    Column("id_carrera", Integer, primary_key=True),
    Column("carrera", String(50))
)

especialidades = Table(
    "especialidades",
    meta,
    Column("id_especialidad", Integer, primary_key=True),
    Column("especialidad", String(50)),
    Column("id_carrera", Integer)
)

materias = Table(
    "materias",
    meta,
    Column("id_materia", Integer, primary_key=True),
    Column("materia", String(50)),
    Column("id_carrera", Integer)
)

alumnos = Table(
    "alumnos",
    meta,
    Column("id_alumno", Integer, primary_key=True),
    Column("apellido_paterno", String(30)),
    Column("apellido_materno", String(30)),
    Column("nombres", String(30)),
    Column("sexo", String(1)),
    Column("curp", String(18)),
    Column("id_carrera", Integer),
    Column("id_especialidad", Integer)
)

calificaciones = Table(
    "calificaciones",
    meta,
    Column("id_calificacion", Integer, primary_key=True),
    Column("calificacion", ), # PENDIENTE REVISAR
    Column("id_alumno", Integer),
    Column("id_materia", Integer)
)

meta.create_all(engine)

# REVISAR FOREIG KEY