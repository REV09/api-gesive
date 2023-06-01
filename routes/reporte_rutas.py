from fastapi import APIRouter, HTTPException, Response
from models.reporte import Reporte
from config.db import conexionDb
from schemas.reporte_esquema import reportes
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_reporte = APIRouter()

@ruta_reporte.get('/reporte', response_model=Reporte, tags=["Reporte"])
def obtener_reporte(id_reporte: int):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.select().where(
        reportes.c.idReporte == id_reporte)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@ruta_reporte.get('/reportes', response_model=list[Reporte], tags=["Reporte"])
def obtener_reportes():
    conexion = conexionDb()
    resultados = conexion.execute(reportes.select()).fetchall()
    conexion.close()
    if resultados:
        return resultados
    
    raise HTTPException(status_code=404, detail="No se encontraron reportes")


@ruta_reporte.post('/reporte', status_code=HTTP_200_OK, tags=["Reporte"])
def agregar_reporte(reporte: Reporte):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.insert().values(reporte.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar reporte")


@ruta_reporte.put('/reporte', status_code=HTTP_200_OK, tags=["Reporte"])
def actualizar_reporte(reporte: Reporte, id_reporte: int):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.update().values(
        idReporte = id_reporte,
        idPoliza = reporte.idPoliza,
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
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar reporte")


@ruta_reporte.delete('/reporte', status_code=HTTP_204_NO_CONTENT, tags=["Reporte"])
def eliminar_reporte(id_reporte: int):
    conexion = conexionDb()
    resultado = conexion.execute(reportes.delete().where(
        reportes.c.idReporte == id_reporte))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar reporte")