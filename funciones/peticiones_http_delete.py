from pydantic import BaseModel
from fastapi import HTTPException, status
from db.client import db_client
from typing import Type, List

def borrar_todos(router, base_de_datos):
    @router.delete("/Eliminar/Todos", status_code=status.HTTP_202_ACCEPTED)
    async def delete_olds():
        coleccion = getattr(db_client, base_de_datos)
        borrados = coleccion.delete_many({"tipo":base_de_datos})
        if not borrados:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="En este momento no hay formatos guardados")