from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from db.models import formato
from db.schemas.formato import formato_schema , formatos_schemas
from bson import ObjectId
from bson.errors import InvalidId


router = APIRouter( prefix="Formato",
                   tags=["Formato"],
                   responses={404:{ "message":"No encontrado"}})

def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")
