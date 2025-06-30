from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status
from db.client import db_client

def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    
def cargar(dato,base_de_datos):
        coleccion = getattr(db_client, base_de_datos)
        if coleccion.find_one({"nombre":dato.nombre_formato}):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El formato que desea cargar ya se encuentra almacenado en nuestra base de datos")
            
        dict_dato = dict(dato)
        del dict_dato["id"]
        return dict_dato