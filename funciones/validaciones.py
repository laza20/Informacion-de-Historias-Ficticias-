from db.client import db_client
from fastapi import HTTPException, status

def validaciones_de_carga_formatos(dato, base_de_datos):
        coleccion = getattr(db_client, base_de_datos)
        if coleccion.find_one({"nombre":dato.nombre_formato}):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El formato que desea cargar ya se encuentra almacenado en nuestra base de datos")
            