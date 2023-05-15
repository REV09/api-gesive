from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.root import rootRoute
from routes.conductor_rutas import ruta_conductor

app = FastAPI(
    title='GESIVE API REST SERVICE',
    description= 'API REST Services for GESIVE clients',
    openapi_tags=[{}]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(rootRoute)
app.include_router(ruta_conductor)