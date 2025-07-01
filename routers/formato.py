from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.formato import Formato
from db.schemas.formato import formato_schema , formatos_schemas
from funciones import funciones_logicas, validaciones
from funciones import peticiones_http_post


router = APIRouter( prefix="/Formatos",
                   tags=["Formatos"],
                   responses={404:{ "message":"No encontrado"}})

#FUNCION PARA CARGAR UN DOCUMENTO    
peticiones_http_post.cargar_uno(
    Formato,
    router,
    "Formatos",
    formato_schema,
    validaciones.validaciones_de_carga_formatos
)

peticiones_http_post.cargar_muchos(
    Formato,
    router,
    "Formatos",
    formatos_schemas,
    validaciones.validaciones_de_carga_formatos
)   

            
@router.delete("/Eliminar/Nombre/{nombre_formato}",status_code=status.HTTP_202_ACCEPTED)
async def delete_one_by_name(nombre_formato:str):
    borrado = db_client.Formatos.find_one_and_delete({"nombre_formato":nombre_formato})
    if not borrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre del formato incorrecto")
    
@router.delete("/Eliminar/Todos", status_code=status.HTTP_202_ACCEPTED)
async def delete_olds():
    borrados = db_client.Formatos.delete_many({"tipo":"Formato"})
    if not borrados:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="En este momento no hay formatos guardados")



@router.get("/Ver/{nombre}")
async def view_for_name(nombre:str):
    try:
        return formato_schema(db_client.Formatos.find_one({"nombre_formato":nombre}))
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El nombre del formato ingresado no se encuentra en la base de datos")
    

@router.get("/Todos", response_model=list[Formato])
async def view_olds_format():
    return formatos_schemas(db_client.Formatos.find())