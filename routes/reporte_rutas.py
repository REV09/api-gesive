from fastapi import APIRouter, HTTPException, Response
from models.reporte import Reporte
from config.db import conexionDb
from schemas.reporte_esquema import reportes
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_reporte = APIRouter()

@ruta_reporte.get('/reporte', response_model=list[Reporte], tags=["Reporte"])
def obtener_reporte(id_reporte: int):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.select().where(
        reportes.c.idReporte == id_reporte)).fetchall()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@ruta_reporte.post('/reporte', response_model=list[Reporte], tags=["Reporte"])
def agregar_reporte(reporte: Reporte):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.insert().values(reporte))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar reporte")


@ruta_reporte.put('/reporte', response_model=list[Reporte], tags=["Reporte"])
def actualizar_reporte(reporte: Reporte, id_reporte: int):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.update().values(
        idReporte = id_reporte,
        posicionLat = reporte.posicionLat,
        posicionLon = reporte.posicionLon,
        involucradosNombres = reporte.involucradosNombres,
        involucradosVehiculos = reporte.involucradosVehiculos,
        fotos = reporte.fotos,
        idAjustador = reporte.idAjustador,
        estatus = reporte.estatus,
        dictamenTexto = reporte.dictamenTexto,
        dictamenFecha = reporte.dictamenFecha,
        dictamenHora = reporte.dictamenHora,
        dictamenFolio = reporte.dictamenFolio
    ).where(reportes.c.idReporte == id_reporte))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar reporte")


@ruta_reporte.delete('/reporte', response_model=list[Reporte], tags=["Reporte"])
def eliminar_reporte(id_reporte: int):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.delete().where(
        reportes.c.idReporte == id_reporte))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar reporte")