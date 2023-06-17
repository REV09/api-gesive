from fastapi import APIRouter, HTTPException, Response
from models.reporte import Reporte
from config.db import conexionDb
from schemas.reporte_esquema import reportes
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from middlewares.verificar_token_rutas import VerificarTokenRutas
from models.reporte import Reporte


ruta_reporte = APIRouter(route_class=VerificarTokenRutas)


@ruta_reporte.get('/reporte', response_model=Reporte, tags=["Reporte"])
def obtener_reporte(id_reporte: int):
    '''
    Metodo para obtener un reporte dado el id de reporte el cual
    debe ser de tipo int

    En caso de encontrar el reporte retorna un objeto de tipo
    Reporte.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(reportes.select().where(
        reportes.c.idReporte == id_reporte)).first()
    conexion.close()
    if resultado:
        reporte_obtenido = Reporte(idReporte=resultado[0], idPoliza=resultado[1],
                                   posicionLat=resultado[2], posicionLon=resultado[3],
                                   involucradosNombres=resultado[4], involucradosVehiculos=resultado[5],
                                   fotos=resultado[6], idAjustador=resultado[7],
                                   estatus=resultado[8], dictamenTexto=resultado[9],
                                   dictamenFecha=resultado[10], dictamenHora=resultado[11],
                                   dictamenFolio=resultado[12])
        reporte_obtenido.decodificar_informacion()
        return reporte_obtenido

    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@ruta_reporte.get('/reportes/usuario', response_model=list[Reporte], tags=["Reporte"])
def obtener_reporte_usuario(id_poliza: int):
    '''
    Metodo para obtener un reporte dado el id de reporte el cual
    debe ser de tipo int

    En caso de encontrar el reporte retorna un objeto de tipo
    Reporte.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    reportes_obtenidos: list[Reporte] = []
    reportes_usuario: list[Reporte] = []
    resultados = conexion.execute(reportes.select()).fetchall()
    conexion.close()
    if resultados:

        for fila in resultados:
            reporte_obtenido = Reporte(idReporte=fila[0], idPoliza=fila[1],
                                       posicionLat=fila[2], posicionLon=fila[3],
                                       involucradosNombres=fila[4], involucradosVehiculos=fila[5],
                                       fotos=fila[6], idAjustador=fila[7],
                                       estatus=fila[8], dictamenTexto=fila[9],
                                       dictamenFecha=fila[10], dictamenHora=fila[11],
                                       dictamenFolio=fila[12])

            reporte_obtenido.decodificar_informacion()
            reportes_obtenidos.append(reporte_obtenido)

        for reporte in reportes_obtenidos:
            if(reporte.idPoliza == id_poliza):
                reportes_usuario.append(reporte)
        
        return reportes_usuario

    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@ruta_reporte.get('/reportes', response_model=list[Reporte], tags=["Reporte"])
def obtener_reportes():
    '''
    Metodo para obtener todos los reportes registrados
    en la base de datos.

    En caso de obtenerlos correctamente retorna una lista de
    objetos de Reporte.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    reportes_obtenidos: list[Reporte] = []
    resultados = conexion.execute(reportes.select()).fetchall()
    conexion.close()
    if resultados:

        for fila in resultados:
            reporte_obtenido = Reporte(idReporte=fila[0], idPoliza=fila[1],
                                       posicionLat=fila[2], posicionLon=fila[3],
                                       involucradosNombres=fila[4], involucradosVehiculos=fila[5],
                                       fotos=fila[6], idAjustador=fila[7],
                                       estatus=fila[8], dictamenTexto=fila[9],
                                       dictamenFecha=fila[10], dictamenHora=fila[11],
                                       dictamenFolio=fila[12])

            reporte_obtenido.decodificar_informacion()
            reportes_obtenidos.append(reporte_obtenido)

        return reportes_obtenidos

    raise HTTPException(status_code=404, detail="No se encontraron reportes")


@ruta_reporte.post('/reporte', status_code=HTTP_200_OK, tags=["Reporte"])
def agregar_reporte(reporte: Reporte):
    '''
    Metodo para agregar un reporte a la base de datos .

    En caso de registrar bien el reporte retorna un codigo 200.

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    reporte.codificar_informacion()
    resultado = conexion.execute(reportes.insert().values(reporte.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al registrar reporte")


@ruta_reporte.put('/reporte', status_code=HTTP_200_OK, tags=["Reporte"])
def actualizar_reporte(reporte: Reporte, id_reporte: int):
    '''
    Metodo para actualizar un repote.

    En caso de actualizar correctamente el reporte retorna un codigo 200

    En caso contrario retorna un codigo 500.
    '''

    conexion = conexionDb()
    reporte.codificar_informacion()
    resultado = conexion.execute(reportes.update().values(
        idReporte=id_reporte,
        idPoliza=reporte.idPoliza,
        posicionLat=reporte.posicionLat,
        posicionLon=reporte.posicionLon,
        involucradosNombres=reporte.involucradosNombres,
        involucradosVehiculos=reporte.involucradosVehiculos,
        fotos=reporte.fotos,
        idAjustador=reporte.idAjustador,
        estatus=reporte.estatus,
        dictamenTexto=reporte.dictamenTexto,
        dictamenFecha=reporte.dictamenFecha,
        dictamenHora=reporte.dictamenHora,
        dictamenFolio=reporte.dictamenFolio
    ).where(reportes.c.idReporte == id_reporte))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al actualizar reporte")


@ruta_reporte.delete('/reporte', status_code=HTTP_204_NO_CONTENT, tags=["Reporte"])
def eliminar_reporte(id_reporte: int):
    '''
    Metodo para eliminar un reporte de la base de datos.

    En caso de eliminar correctamente el reporte retorna un codigo 204

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(reportes.delete().where(
        reportes.c.idReporte == id_reporte))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=500, detail="Error del servidor al eliminar reporte")
