from typing import List
from uuid import uuid4
from fastapi import FastAPI
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

@app.get("/api/v1/usuario")
async def buscaUsuarios():
    return db;

@app.post("/api/v1/usuario")
async def registrar_usuario(usuario: Usuario):
    db.append(usuario)
    return {"id_usuario": usuario.id}