from db.client import db_client
from fastapi import HTTPException, status

def validaciones_de_carga_formatos(dato, base_de_datos):
    coleccion = getattr(db_client, base_de_datos)
    if coleccion.find_one({"nombre_formato":dato.nombre_formato}):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El formato que desea cargar ya se encuentra almacenado en nuestra base de datos")
            
            
def validaciones_de_carga_historias(dato, base_de_datos):
    coleccion = getattr(db_client, base_de_datos)
    filtros = {
        "nombre_de_la_historia":{"$regex": f"^{dato.nombre_de_la_historia}$", "$options": "i"},
        "year": {"$regex": f"^{dato.year}$", "$options": "i"},
        "formato":{"$regex": f"^{dato.formato}$", "$options": "i"}
        }
    if coleccion.find_one(filtros):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="La historia ingresada ya se encuentra en nuestra base de datos")
    
    if not db_client.Formatos.find_one({"nombre_formato":{"$regex": f"^{dato.formato}$", "$options": "i"}}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El formato {dato.formato} ingresado es incorrecto o no se encuentra en la base de datos")
        
def validacion_de_carga_caracteristicas(dato, base_de_datos):
    coleccion = getattr(db_client, base_de_datos)
    filtro_historia = {        
        "nombre_de_la_historia":{"$regex": f"^{dato.nombre_historia}$", "$options": "i"},
        "formato":{"$regex": f"^{dato.formato}$", "$options": "i"}
    }
    
    filtro = {
        "caracteristica":{"$regex": f"^{dato.caracteristica}$", "$options": "i"},
        "nombre_historia":{"$regex": f"^{dato.nombre_historia}$", "$options": "i"},
        "formato":{"$regex": f"^{dato.formato}$", "$options": "i"},
        "identificacion":{"$regex": f"^{dato.identificacion}$", "$options": "i"}
    }
    if not db_client.Formatos.find_one({"nombre_formato":{"$regex": f"^{dato.formato}$", "$options": "i"}}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El formato {dato.formato} ingresado es incorrecto o no se encuentra en la base de datos")
    
    if not db_client.Historias.find_one(filtro_historia):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="La historia ingresada no se encuentra en nuestra base de datos")
    
    if coleccion.find_one(filtro):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Caracteristica existente en la Base de datos")
    