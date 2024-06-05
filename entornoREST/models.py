from pydantic import BaseModel, Field

class recicInsert(BaseModel):
    nombre:str
    precio:str
    comentario:str
class recicInactivo(BaseModel):
    estatus:str=Field(default='DESACTIVADO')
    motivoCancelacion:str
class recicUpdate(BaseModel):
    nombre:str
    precio:str
    comentario:str
class reciclableBd(recicInsert):
    id: str