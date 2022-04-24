from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Regras, Sexo, User

app = FastAPI()

db: List[User] = [
    User (id=uuid4(), 
    nome="Jamila", 
    sobrenome ="Araujo",
    sexo = Sexo.feminino,
    regras = [Regras.student]),

    User (id=uuid4(), 
    nome="Jonas", 
    sobrenome ="Sousa",
    sexo = Sexo.masculino,
    regras = [Regras.admin, Regras.user])
]

@app.get("/")
def home():
    return {"message": "hello World! Servidor python"}

@app.get("/perfil")
def perfil():
    return {"Nome": "Hemerson chaves"}
