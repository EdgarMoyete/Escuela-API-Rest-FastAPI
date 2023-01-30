from fastapi import FastAPI

from routes.carreras import carre
# from routes.especialidades import espec

app = FastAPI(
    title = "API Rest de Escuela",
    description = "API Rest para un CRUD de escuela",
    version = "0.0.1",
    openapi_tags = [
        {
            "name": "Escuela",
            "description": "Carreras, Especialidades, Materias, Alumnos y Calificaciones"
        }
    ],
    contact={
        "name": "Edgar Moises Hernandez-Gonzalez",
        "url": "https://github.com/EdgarMoyete",
        "email": "edgar.hernandez@crediclub.com"
    },
    license_info= {
        "name": "MIT License",
    }
)

@app.get("/")
async def index():
    return {"Bienvenido a mi API Rest de Escuela"}

app.include_router(carre)
# app.include_router(espec)