def formato_schema (tipo)->dict:
        return {
            "id"                  : str(tipo["_id"]),
            "nombre_formato"      : str(tipo["nombre_formato"]).title().strip(),
            "descripcion"         : str(tipo["descripcion"]).strip(),
            "tipo"                : str(tipo["tipo"]).capitalize().strip()
            }
        
def formatos_schemas(tipos)->list:
    return [formato_schema(tipo) for tipo in tipos]