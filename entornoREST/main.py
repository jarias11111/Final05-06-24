from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def inicio ():
    return {"mensaje":"Bienvenido a devOpsREST "}