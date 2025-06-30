def caracterica_schema(tipo)->dict:
    return{
    "id"             : str (tipo["_id"]),
    "caracteristica" : str (tipo["caracteristica"]),
    "descripcion"    : str (tipo["descripcion"]),
    "nombre_historia": str (tipo["nombre_historia"]),
    "formato"        : str (tipo["formato"]),
    "tipo"           : str (tipo["tipo"]),
    }
    
def caractericas_schema(tipos)->(list):
    return [caracterica_schema(tipo) for tipo in tipos]