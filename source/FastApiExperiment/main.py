from fastapi import FastAPI

app = FastAPI()

#Este comando vai exibir "Hello, World!" na raiz da aplicação
@app.get("/")
async def root():
    return {"message": "Hello, World!"}

#Este endpoint recebe um nome como parâmetro e retorna uma saudação personalizada
@app.get("/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}! - {type(name)}"}

"""
Este é um exemplo simples de uma aplicação FastAPI com dois endpoints:
1. O endpoint raiz ("/") que retorna uma mensagem "Hello, World!".
2. O endpoint "/{name}" que retorna uma saudação personalizada com o nome fornecido
    na URL.
Versão 0.1
"""