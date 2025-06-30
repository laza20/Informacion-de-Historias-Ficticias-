from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException, status

def validate_object_id(id: str):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")