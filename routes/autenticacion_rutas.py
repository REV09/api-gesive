from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from models.empleado import Empleado
from routes.empleado_rutas import autenticar_empleado
from security.auth import escribir_token, valida_token


auth_rutas = APIRouter()

@auth_rutas.post('/autenticacion/empleado', tags=["Autenticacion"])
def validar_empleado(empleado: Empleado):

    '''
    Este es el metodo para autenticar el login de un empleado, este
    metodo usa tambien el metodo autenticar_empleado que recibe como
    argumentos un objeto de tipo empleado.
    
    Si la respuesta recibida es un codigo 200 el empleado es valido
    y retorna un token JWT.
    '''

    respuesta = autenticar_empleado(empleado)

    if(respuesta.status_code == 200):
        return escribir_token(empleado.dict())
    
    else:
        return JSONResponse(content={"message": "usuario o contraseña no encontrado"}, status_code=404)
    

@auth_rutas.post('/autenticacion/token', tags=["Autenticacion"])
def validar_token(Authorization: str = Header(None)):

    '''
    Este metodo se encarga de validar el token recibido, para eso se
    recibe el token de la cabecera Authorization, y se manda a llamar
    al metodo valida_token que recibe el token y este caso se le envia
    True al argumento output para especificar que si se le regrese el
    contenido decodificado del token en el caso de ser valido.
    '''

    token = Authorization.split(" ")[1]
    return valida_token(token, output=True)
