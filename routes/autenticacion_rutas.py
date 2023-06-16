from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from models.empleado import Empleado
from models.conductor import Conductor
from routes.empleado_rutas import autenticar_empleado, obtener_empleado_por_username
from routes.conductor_rutas import autenticar_conductor, obtener_conductor_por_numero_telefono
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

    if (respuesta.status_code == 200):
        datos_empleado = obtener_empleado_por_username(empleado.nombreUsuario)
        return escribir_token(datos_empleado.dict())

    else:
        return JSONResponse(content={"message": "usuario o contraseña no encontrado"}, status_code=404)


@auth_rutas.post('/autenticacion/conductor', tags=["Autenticacion"])
def validar_conductor(conductor: Conductor):
    '''
    Este es el metodo para autenticar el login de un conductor, este
    metodo usa tambien el metodo `autenticar_conductor`.

    Que recibe como argumentos un objeto de tipo `Conductor`.
    Si la respuesta recibida es un codigo 200 el el conductor es valido
    y retornara un token JWT
    '''

    respuesta = autenticar_conductor(conductor)

    if (respuesta.status_code == 200):
        datos_conductor = obtener_conductor_por_numero_telefono(conductor.telefono)
        return escribir_token(datos_conductor.dict())

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
