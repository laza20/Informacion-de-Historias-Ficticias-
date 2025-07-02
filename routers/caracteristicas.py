from fastapi import APIRouter
from db.models.caracteristicas import Caracteristicas
from db.schemas.caracteristicas import caracterica_schema,caractericas_schema
from funciones import  peticiones_http_post, validaciones, peticiones_http_get

router = APIRouter(prefix="/Caracteristicas",
                   tags= ["Caracteristicas"],
                   responses={404:{"message":"No encontrado"}}
)

peticiones_http_post.cargar_uno(
    Caracteristicas,
    router,
    "Caracteristicas",
    caracterica_schema,
    validaciones.validacion_de_carga_caracteristicas
)

peticiones_http_post.cargar_muchos(
    Caracteristicas,
    router,
    "Caracteristicas",
    caractericas_schema,
    validaciones.validacion_de_carga_caracteristicas    
)

peticiones_http_get.ver_todos(
    router, 
    Caracteristicas, 
    caractericas_schema, 
    "Caracteristicas"
)


lista_propiedades_sigulares = ["caracteristica", "descripcion", ]
peticiones_http_get.ver_uno_por_dato_string(
    router, 
    caracterica_schema, 
    "Caracteristicas", 
    lista_propiedades_sigulares
)

lista_propiedades_plurales = ["nombre_historia","formato","identificacion"]
peticiones_http_get.ver_documentos_por_filtro(
    router, 
    caractericas_schema, 
    "Caracteristicas", 
    lista_propiedades_plurales
)