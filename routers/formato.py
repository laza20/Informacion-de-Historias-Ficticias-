from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.formato import Formato
from db.schemas.formato import formato_schema , formatos_schemas
from funciones import validaciones
from funciones import peticiones_http_post, peticiones_http_get, peticiones_http_delete


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

peticiones_http_get.ver_todos(
    router, 
    Formato, 
    formatos_schemas, 
    "Formatos"
)

lista_propiedades_sigulares = ["nombre_formato", "descripcion"]
peticiones_http_get.ver_uno_por_dato_string(
    router, 
    formato_schema, 
    "Formatos", 
    lista_propiedades_sigulares
)

peticiones_http_delete.borrar_todos(
    router,
    "Formatos"
    )


@router.delete("/Eliminar/Nombre/{nombre_formato}",status_code=status.HTTP_202_ACCEPTED)
async def delete_one_by_name(nombre_formato:str):
    borrado = db_client.Formatos.find_one_and_delete({"nombre_formato":nombre_formato})
    if not borrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre del formato incorrecto")
    
