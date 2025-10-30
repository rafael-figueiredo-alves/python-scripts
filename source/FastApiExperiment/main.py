from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/{name}")
async def greet(name: str):
    return {"message": f"Hello, {name}!"}