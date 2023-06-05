from fastapi.routing import APIRoute
from fastapi import Request
from security.auth import valida_token

class VerificarTokenRutas(APIRoute):

    def get_route_handler(self):

        '''
        Este metodo se encarga de hacer que cada una de las rutas de
        la API requieran de un token de autenticacion para
        autorizar el consumo del servicio
        '''

        original_ruta = super().get_route_handler()
    
        async def verify_token_middleware(request: Request):
            token = request.headers["Authorization"].split(" ")[1]
            validation_response = valida_token(token, output=False)

            if validation_response == None:
                return await original_ruta(request)
            
            else:
                return validation_response
            
        return verify_token_middleware