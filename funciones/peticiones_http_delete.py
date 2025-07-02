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
        
def borrar_por_data_string(router, base_de_datos, lista_propiedades):
    @router.delete("/Eliminar/Por/{dato}",status_code=status.HTTP_202_ACCEPTED)
    async def delete_by_data(dato:str):
        coleccion = getattr(db_client, base_de_datos)
        for propiedad in lista_propiedades:
            borrado = coleccion.find_one_and_delete({propiedad:dato})
            if borrado:
                return {"mensaje": f"Documento con {propiedad} = '{dato}' eliminado correctamente"}
        
        if not borrado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Dato {dato} incorrecto")