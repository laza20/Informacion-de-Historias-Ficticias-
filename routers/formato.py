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

lista_propiedades_sigulares_a_borrar = ["nombre_formato", "descripcion"]
peticiones_http_delete.borrar_por_data_string(
    router,
    "Formatos",
    lista_propiedades_sigulares_a_borrar
)
    
