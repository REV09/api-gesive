from fastapi import APIRouter, HTTPException, Response, UploadFile, File
from fastapi.responses import Response
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from config.db import conexionDb
from models.foto import Foto
from schemas.foto_esquema import fotos
from images.convertir_fotos import obtener_binarios_fotos, crear_foto, guardar_foto, leer_foto


ruta_foto = APIRouter()

@ruta_foto.get('/fotos', tags=["Foto"])
def obtener_foto_reporte(id_foto: int):

    '''
    Ruta para obtener las fotos guardadas de un reporte.

    EL id del reporte recibido debe ser de tipo int para no producir un error en el servidor

    En el caso de que la consulta sea exitosa retornara un listado con todas las fotos
    registradas en el reporte.

    En el caso contrario retornara un 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(fotos.select().where(fotos.c.idfoto == id_foto)).first()
    if resultado:
        guardar_foto(resultado[1])
        blob_foto = leer_foto()
        
        return Response(content=blob_foto, media_type="image/jpeg")
    
    raise HTTPException(status_code=404, detail="No se encontraron fotos")


@ruta_foto.post('/fotos', status_code=HTTP_200_OK, tags=["Foto"])
async def agregar_foto(archivo: UploadFile = File(...), id_reporte: int = 0):

    '''
    Metodo para agregar las fotos de un reporte

    En caso de que se agregen correctamente se retornara un 200

    En caso contrario se retornara un 500
    '''

    datos = await archivo.read()
    foto = crear_foto(datos_foto=datos, id_reporte=id_reporte)
    conexion = conexionDb()
    resultado = conexion.execute(fotos.insert().values(foto.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al guardar la foto")
    

@ruta_foto.delete('/fotos', status_code=HTTP_204_NO_CONTENT, tags=["Foto"])
def eliminar_foto(id_reporte: int):

    '''
    Metodo para eliminar las fotos de un reporte

    En caso de que se eliminen correctamente se retornara un 204

    En caso contrario se retornara un 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(fotos.delete().where(
        fotos.c.idReporte == id_reporte))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar fotos")