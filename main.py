from fastapi import FastAPI
from routers import formato


app = FastAPI()

app.include_router(formato.router)