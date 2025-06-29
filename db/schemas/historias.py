def historia_schema (tipo)->dict:
        return {
            "id"                         : str(tipo["_id"]),
            "nombre_de_la_historia"      : str(tipo["nombre_de_la_historia"]).title().strip(),
            "descripcion"                : str(tipo["descripcion"]).strip(),
            "year"                       : int(tipo["year"]),
            "formato"                    : str(tipo["formato"]).title().strip(),
            "tipo"                       : str(tipo["tipo"]).capitalize().strip()
            }
        
def historias_schema(tipos)->list:
    return [historia_schema(tipo) for tipo in tipos]