from fastapi import FastAPI
import uvicorn
from objectAccessData import Conexion
from models import recicInsert, recicInactivo, recicUpdate

app = FastAPI()

@app.get('/')
def inicio ():
    return {"mensaje":"Bienvenido a ecoSwap-14 "}

@app.on_event('startup')
def startup():
    app.cn=Conexion()
    print("Conectando con la BD")

@app.on_event('shutdown')
def shutdown():
    app.cn.cerrar()
    print("Cerrando la Conexión")
@app.post('/reciclables', tags=["RECICLABLE REST"])
def agregarReciclable (recicla:recicInsert):
    salida=app.cn.agregarReciclable(recicla)
    return salida
@app.delete('/reciclables/{idReciclable}/cancelar', tags=["RECICLABLE REST"])
def cancelarReciclable (idReciclable:str,cancelar:recicInactivo):
    salida=app.cn.cancelarReciclable(idReciclable,cancelar)
    return salida
@app.put('/reciclables/{idReciclable}/modificar', tags=["RECICLABLE REST"])
def modificarReciclable(idReciclable:str, modificar: recicUpdate):
    salida = app.cn.modificarReciclable(idReciclable, modificar)
    return salida