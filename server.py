from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello World! Servidor python"}

@app.get("/perfil")
def perfil():
    return {"Nome": "Hemerson chaves"}
