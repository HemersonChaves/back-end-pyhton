from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel

class Sexo(str, Enum):
    masculino = "masculino"
    feminino = "feminino"
    
class Regras(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    nome: str
    sobrenome: str
    sexo: Sexo
    regras: List[Regras]
