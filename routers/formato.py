from fastapi import FastAPI
from db.client import db_client
from db.models import formato
from db.schemas.formato import formato_schema , formatos_schemas
from bson import ObjectId
from bson.errors import InvalidId