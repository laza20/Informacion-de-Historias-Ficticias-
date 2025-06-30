from fastapi import FastAPI
from routers import formato, historias, caracteristicas


app = FastAPI()

app.include_router(formato.router)
app.include_router(historias.router)
app.include_router(caracteristicas.router)