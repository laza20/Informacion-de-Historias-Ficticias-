# pyright: reportInvalidTypeForm=false
from pydantic import BaseModel
from fastapi import HTTPException, status
from db.client import db_client
from typing import Type, List

def ver_todos(router, Clase: Type[BaseModel], schema, base_de_datos):
    @router.get("/Todos", response_model=List[Clase])
    async def view_olds():
        coleccion = getattr(db_client, base_de_datos)
        datos = schema(list(coleccion.find({"tipo": base_de_datos})))
        if not datos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se encontraron o no hay datos")
        
        return datos