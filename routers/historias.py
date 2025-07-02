from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.historias import Historias
from db.schemas.historias import historia_schema, historias_schema
from funciones import validaciones, peticiones_http_post, peticiones_http_get, peticiones_http_delete

router = APIRouter( prefix="/Historias",
                   tags=["Historias"],
                   responses={404:{ "message":"No encontrado"}})
    

#FUNCION PARA CARGAR UN DOCUMENTO 
peticiones_http_post.cargar_uno(
    Historias,
    router,
    "Historias",
    historia_schema,
    validaciones.validaciones_de_carga_historias
)

peticiones_http_post.cargar_muchos(
    Historias,
    router,
    "Historias",
    historias_schema,
    validaciones.validaciones_de_carga_historias    
)

peticiones_http_get.ver_todos(
    router, 
    Historias, 
    historias_schema, 
    "Historias"
)
    
lista_propiedades_sigulares = ["nombre_de_la_historia", "descripcion"]
peticiones_http_get.ver_uno_por_dato_string(
    router, 
    historia_schema, 
    "Historias", 
    lista_propiedades_sigulares
)

lista_propiedades_sigulares_int = ["year"]
peticiones_http_get.ver_documento_por_año(
    router, 
    historias_schema, 
    "Historias", 
    lista_propiedades_sigulares_int
)

lista_propiedades_plurales = ["formato"]
peticiones_http_get.ver_documentos_por_filtro(
    router, 
    historias_schema, 
    "Historias", 
    lista_propiedades_plurales
)

peticiones_http_delete.borrar_todos(
    router,
    "Historias"
    )

lista_propiedades_sigulares_a_borrar = ["nombre_de_la_historia", "descripcion"]
peticiones_http_delete.borrar_por_data_string(
    router,
    "Historias",
    lista_propiedades_sigulares_a_borrar
)