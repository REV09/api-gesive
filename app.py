from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes.autenticacion_rutas import auth_rutas
from routes.conductor_rutas import ruta_conductor, ruta_registrar_conductor
from routes.vehiculo_rutas import ruta_vehiculo
from routes.empleado_rutas import ruta_empleado
from routes.pago_rutas import ruta_pagos
from routes.poliza_rutas import ruta_poliza
from routes.reporte_rutas import ruta_reporte
from routes.foto_rutas import ruta_foto

app = FastAPI(
    title='GESIVE API REST SERVICE',
    description= 'API REST Services for GESIVE clients',
    openapi_tags=[{
        'name':'Conductor',
        'description': 'rutas de servicios REST para conductor'},
        {'name': 'Empleado',
         'description': 'rutas de servicios REST para empleado'},
        {'name': 'Pago',
         'description': 'rutas de servicios REST para pago'},
        {'name': 'Poliza',
         'description': 'rutas de servicios REST para poliza'},
        {'name': 'Reporte',
         'description': 'rutas de servicios REST para reporte'},
        {'name': 'Vehiculo',
         'description': 'rutas de servicios REST para vehiculo'},
         ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_rutas)
app.include_router(ruta_conductor)
app.include_router(ruta_vehiculo)
app.include_router(ruta_empleado)
app.include_router(ruta_pagos)
app.include_router(ruta_poliza)
app.include_router(ruta_reporte)
app.include_router(ruta_foto)
app.include_router(ruta_registrar_conductor)
load_dotenv()
