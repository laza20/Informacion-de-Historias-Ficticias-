from pydantic import BaseModel

class Caracteristicas(BaseModel):
    id             : str | None = None
    caracteristica : str
    descripcion    : str
    nombre_historia: str
    formato        : str
    identificacion : str
    tipo           : str 