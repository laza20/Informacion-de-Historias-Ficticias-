from pydantic import BaseModel

class Formato(BaseModel):
    id                       : str | None = None
    nombre_formato           : str
    descripcion              : str