from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.historias import Historias
from db.schemas.historias import historia_schema, historias_schema
from funciones import funciones_logicas, validaciones

router = APIRouter( prefix="/Historias",
                   tags=["Historias"],
                   responses={404:{ "message":"No encontrado"}})
    
@router.post("/Cargar/Uno", response_model=Historias, status_code=status.HTTP_201_CREATED)
async def create_one(historia:Historias):
    validaciones.validaciones_de_carga_historias(historia, "Historias")
    new_historia = funciones_logicas.cargar_uno(historia, "Historias", historia_schema)
    
    return new_historia

@router.post("/Cargar/Muchos", response_model=list[Historias], status_code=status.HTTP_201_CREATED)
async def create_many(historias:list[Historias]):
    
    documentos = funciones_logicas.cargar_muchos(historias, "Historias", historias_schema, validaciones.validaciones_de_carga_historias)
    return documentos

    
@router.get("/Todos", response_model=list[Historias])
async def view_olds():
    return historias_schema(db_client.Historias.find({"tipo":"historia"}))

@router.get("/Ver/{nombre_de_la_historia}")
async def view_by_name(nombre_de_la_historia:str):
    return historia_schema(db_client.Historias.find_one({"nombre_de_la_historia":{"$regex": f"^{nombre_de_la_historia}$", "$options": "i"}}))

@router.delete("/Eliminar/Todos", status_code=status.HTTP_202_ACCEPTED)
async def delete_olds():
    borrados = db_client.Historias.delete_many({"tipo":"Historia"})
    if not borrados:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="En este momento no hay formatos guardados")

@router.delete("/Eliminar/Nombre/{nombre_de_la_historia}",status_code=status.HTTP_202_ACCEPTED)
async def delete_one_by_name(nombre_de_la_historia:str):
    borrado = db_client.Historias.find_one_and_delete({"nombre_de_la_historia":nombre_de_la_historia})
    if not borrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre del formato incorrecto")