from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.caracteristicas import Caracteristicas
from db.schemas.caracteristicas import caracterica_schema,caractericas_schema
from funciones import funciones_logicas, peticiones_http_post, validaciones

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
