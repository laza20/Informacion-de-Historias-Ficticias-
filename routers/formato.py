from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models.formato import Formato
from db.schemas.formato import formato_schema , formatos_schemas
from bson import ObjectId
from bson.errors import InvalidId


router = APIRouter( prefix="/Formatos",
                   tags=["Formatos"],
                   responses={404:{ "message":"No encontrado"}})

def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
    
@router.post("/Cargar/Uno",response_model=Formato, status_code=status.HTTP_200_OK)
async def create_one(formato:Formato):
    
    if db_client.Formatos.find_one({"nombre_formato":formato.nombre_formato}):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El formato que desea cargar ya se encuentra almacenado en nuestra base de datos")
    
    dict_formato = dict(formato)
    del dict_formato["id"]
    dict_formato["tipo"] = "Formato"
    
    id = db_client.Formatos.insert_one(dict_formato).inserted_id
    new_formato = formato_schema(db_client.Formatos.find_one({"_id":id}))
    return new_formato


@router.post("/Cargar/Muchos", response_model=list[Formato], status_code=status.HTTP_200_OK)
async def create_many(formatos:list[Formato]):
    lista_formatos = []
    for formato in formatos:
            if db_client.Formatos.find_one({"nombre":formato.nombre_formato}):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El formato que desea cargar ya se encuentra almacenado en nuestra base de datos")
            
            dict_formato = dict(formato)
            del dict_formato["id"]
            dict_formato["tipo"] = "Formato"
            lista_formatos.append(dict_formato)
        
    resultado = db_client.Formatos.insert_many(lista_formatos)
    ids = resultado.inserted_ids
    documentos = db_client.Formatos.find({"_id":{"$in":ids}})
    return formatos_schemas(documentos)
            
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