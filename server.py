from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Regras, Sexo, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario (
    id=uuid4(), 
    nome="Jamila", 
    sobrenome ="Araujo",
    sexo = Sexo.feminino,
    regras = [Regras.student]),

    Usuario (
    id=uuid4(), 
    nome="Jonas", 
    sobrenome ="Sousa",
    sexo = Sexo.masculino,
    regras = [Regras.admin, Regras.user])
]

@app.get("/")
async def home():
    return {"message": "hello World! Servidor python"}

@app.get("/api/v1/usuarios")
async def buscaUsuarios():
    return db;

@app.post("/api/v1/usuarios")
async def registrarUsuario(usuario: Usuario):
    db.append(usuario)
    return {"id_usuario": usuario.id}

@app.delete("/api/v1/usuarios/{id_usuario}")
async def excluiUsuario(id_usuario: UUID):
    for usuario in db:
        if usuario.id == id_usuario:
            db.remove(usuario)
            return
    raise HTTPException(
        status_code = 404,
        detail=f"Usuario com o id: {id_usuario} não existe"
    )
        