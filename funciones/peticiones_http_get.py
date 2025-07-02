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
    
    
def ver_uno_por_dato_string(router, schema, base_de_datos, lista_proiedades):
    @router.get("/Ver/{dato}")
    async def view_by_data(dato:str):
        coleccion = getattr(db_client, base_de_datos)
        for propiedad in lista_proiedades:
            resultado = coleccion.find_one({propiedad:{"$regex": f"^{dato}$", "$options": "i"}})
            if resultado:
                return schema(resultado)
                
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se han encontrado documentos con el dato {dato}")
        
def ver_uno_por_dato_year(router, schema, base_de_datos, lista_proiedades):
    @router.get("/Ver/Año/{dato}")
    async def view_by_year(dato:int):
        coleccion = getattr(db_client, base_de_datos)
        for propiedad in lista_proiedades:
            resultado = schema(coleccion.find({propiedad:dato}))
            if resultado:
                return resultado
                
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No se han encontrado documentos con el Año {dato}")
        