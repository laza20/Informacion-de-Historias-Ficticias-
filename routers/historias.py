from fastapi import APIRouter, HTTPException, status
from db.client import db_client
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter( prefix="/Historias",
                   tags=["Historias"],
                   responses={404:{ "message":"No encontrado"}})


def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")