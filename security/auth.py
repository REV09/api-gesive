from jwt import encode, decode
from jwt import exceptions
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from security.encriptacion import cargar_llave

KEY = cargar_llave()

def expiracion_fecha(days: int):

    '''
    Este metodo se encarga de crear la fecha de expiracion del token
    usado para JWT y retorn la fecha de expiracion
    '''

    fecha = datetime.now()
    nueva_fecha = fecha + timedelta(days)
    return nueva_fecha

def escribir_token(data: dict):

    '''
    Este metodo se encarga de crear el token de verificacion para el
    consumo de la API sin este token la mayoria de los metodos de la
    API no se pueden consumir, para la creacion del token se usa, la
    informacion recibida en data, la fecha de expiracion, la llave
    de encriptacion y el algoritmo especificado en el encode.
    Este metodo retorna el token creado
    '''

    token = encode(payload={**data, "exp": expiracion_fecha(1)}, key=KEY, algorithm="HS256")
    return token

def valida_token(token, output=False):

    '''
    Este metodo se encarga de validar el token recibido, recibe
    ademas otro parametro llamado output que se encarga de validar
    si el metodo debe regresar la informacion del token decodificada
    o si solo es necesario validar el token.

    Si se obtiene una excepcion de tipo DecodeError signifca que el 
    token es invalido y se retornara un 401 con el mensaje: token
    invalido.

    Si se obtiene una excepcion de tipo ExpiredSignatureError
    significa que el token esta expirado y se retornara un 401 con
    el mensaje: token expirado.
    '''

    try:
        if output:
            return decode(token, key=KEY, algorithms=["HS256"])

        decode(token, key=KEY, algorithms=["HS256"])

    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Token Invalido"}, status_code=401)
    
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expirado"}, status_code=401)