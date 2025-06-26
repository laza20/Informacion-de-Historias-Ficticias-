from pydantic import BaseModel

class Historias(BaseModel):
    id                       : str | None = None
    nombre_de_la_historia    : str
    descripcion              : str
    year                     : int
    formato                  : str
    tipo                     : str | None = None