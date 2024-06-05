from pymongo import MongoClient
from models import recicInsert, recicInactivo, recicUpdate
from bson import ObjectId

class Conexion():
    def __init__(self):
        self.cliente=MongoClient()
        self.bd=self.cliente.ecoSwap14
    def cerrar(self):
        self.cliente.close()
    def agregarReciclable(self,reciclable:recicInsert):
        respuesta={"estatus":"","mensaje":""}
        if reciclable:
                    res=self.bd.reciclable.insert_one(reciclable.dict())
                    respuesta["estatus"]="OK"
                    respuesta["mensaje"]="Reciclable agregado con id"+str(res)
                    respuesta["Usuario"]=reciclable
        else:
                    respuesta["estatus"]="Error"
                    respuesta["mensaje"]="El Reciclable no se agregó"
        return respuesta
    def cancelarReciclable(self,idReciclable,cancelacion:recicInactivo): 
        resp={"estatus":"","mensaje":""}
        self.bd.reciclable.update_one(
                    {"_id": ObjectId(idReciclable)},
                    {"$set": {"estatus": "INACTIVO"}}
                )
        resp["estatus"]="Ok"
        resp["mensaje"]=f"Reciclable desactivado con id:{idReciclable}"  
        return  resp
    def modificarReciclable(self,idReciclable,modificar:recicUpdate):
        resp={"estatus":"","mensaje":""}
        self.bd.reciclable.update_one(
                    {"_id": ObjectId(idReciclable)},
                    {"$set": {"estatus": "A",
                              "nombre":modificar.nombre,
                              "precio":modificar.precio,
                              "comentario":modificar.comentario,}}
            )
        resp["estatus"]="Ok"
        resp["mensaje"]=f"Reciclable modificado en datos generales con id:{idReciclable}"  
        return  resp