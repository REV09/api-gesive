from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

rootRoute = APIRouter()

@rootRoute.get('/root', status_code=HTTP_204_NO_CONTENT)
def get_root():
    return Response(status_code=HTTP_204_NO_CONTENT)