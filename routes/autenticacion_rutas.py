from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from models.empleado import Empleado
from routes.empleado_rutas import autenticar_empleado
from security.auth import escribir_token, valida_token


auth_rutas = APIRouter()

@auth_rutas.post('/autenticacion/empleado', tags=["Autenticacion"])
def validar_empleado(empleado: Empleado):
    respuesta = autenticar_empleado(empleado)

    if(respuesta.status_code == 200):
        return escribir_token(empleado.dict())
    
    else:
        return JSONResponse(content={"message": "usuario o contraseña no encontrado"}, status_code=404)
    

@auth_rutas.post('/autenticacion/token', tags=["Autenticacion"])
def validar_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return valida_token(token, output=True)
