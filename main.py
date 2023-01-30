from fastapi import FastAPI

from routes.carreras import carre
from routes.especialidades import espec

app = FastAPI(
    # title = "API de Usuarios",
    # description = "API Rest para un CRUD de usuarios",
    # version = "0.0.1",
    # openapi_tags = [
    #     {
    #         "name": "users",
    #         "description": "users routes"
    #     }
    # ]
)

@app.get("/")
async def index():
    return {"Bienvenido a mi API Rest de Escuela"}

app.include_router(carre)
app.include_router(espec)