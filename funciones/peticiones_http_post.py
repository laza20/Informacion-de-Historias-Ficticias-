# pyright: reportInvalidTypeForm=false
from funciones import funciones_logicas
from fastapi import status, Body
from pydantic import BaseModel
from typing import Type, Any



def cargar_uno(Clase: Type[BaseModel], router, base_de_datos, schema, validacion):
    @router.post("/Cargar/Uno", response_model=Clase, status_code=status.HTTP_201_CREATED)
    async def create_one(clase: Clase = Body(...)):
        validacion(clase, base_de_datos)
        new_document = funciones_logicas.cargar_uno(clase, base_de_datos, schema)
    
        return new_document