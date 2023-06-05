from jwt import encode, decode
from jwt import exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse
from security.encriptacion import cargar_llave

KEY = cargar_llave()

def expiracion_fecha(days: int):
    fecha = datetime.now()
    nueva_fecha = fecha + timedelta(days)
    return nueva_fecha

def escribir_token(data: dict):
    token = encode(payload={**data, "exp": expiracion_fecha(1)}, key=KEY, algorithm="HS256")
    return token

def valida_token(token, output=False):
    try:
        if output:
            return decode(token, key=KEY, algorithms=["HS256"])

        decode(token, key=KEY, algorithms=["HS256"])

    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Token Invalido"}, status_code=401)
    
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expirado"}, status_code=401)