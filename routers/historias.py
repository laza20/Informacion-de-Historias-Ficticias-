from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from bson import ObjectId
from bson.errors import InvalidId
from db.models.historias import Historias
from db.schemas.historias import historia_schema, historias_schema

router = APIRouter( prefix="/Historias",
                   tags=["Historias"],
                   responses={404:{ "message":"No encontrado"}})


def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    
@router.post("/Cargar/Uno", response_model=Historias, status_code=status.HTTP_201_CREATED)
async def create_one(historia:Historias):
    dict_historia = cargar(historia)
    
    id = db_client.Historias.insert_one(dict_historia).inserted_id
    new_historia = historia_schema(db_client.Historias.find_one({"_id":id}))
    
    return new_historia

@router.post("/Cargar/Muchos", response_model=list[Historias], status_code=status.HTTP_201_CREATED)
async def create_many(historias:list[Historias]):

    lista_historias = []
    for historia in historias:
        dict_historia = cargar(historia)
        lista_historias.append(dict_historia)
        
    resultado = db_client.Historias.insert_many(lista_historias)
    ids = resultado.inserted_ids
    documentos = db_client.Historias.find({"_id":{"$in":ids}})
    
    return historias_schema(documentos)

def cargar(historia):
        filtros = {
            "nombre_de_la_historia":historia.nombre_de_la_historia,
            "year": historia.year,
            "formato":historia.formato
            }
        if db_client.Historias.find_one(filtros):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="La historia ingresada ya se encuentra en nuestra base de datos")
    
        if not db_client.Formatos.find_one({"nombre_formato":historia.formato}):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El formato ingresado es incorrecto o no se encuentra en la base de datos")
        
        dict_historia = dict(historia)
        del dict_historia["id"]
        dict_historia["tipo"] = "historia"
        return dict_historia