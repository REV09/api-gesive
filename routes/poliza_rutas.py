from fastapi import APIRouter, HTTPException, Response
from models.poliza import Poliza
from config.db import conexionDb
from schemas.poliza_esquema import polizas
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from middlewares.verificar_token_rutas import VerificarTokenRutas


ruta_poliza = APIRouter(route_class=VerificarTokenRutas)


@ruta_poliza.get('/poliza', response_model=Poliza, tags=["Poliza"])
def obtener_poliza(id_poliza: int):
    '''
    Metodo para obtener una poliza dado el id de poliza el cual
    debe ser de tipo int

    En caso de encontrar la poliza retorna un objeto de tipo
    Poliza.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(polizas.select().where(
        polizas.c.idpoliza == id_poliza)).first()
    conexion.close()
    if resultado:
        return resultado

    raise HTTPException(status_code=404, detail="poliza no encontrada")


@ruta_poliza.get('/polizas', response_model=list[Poliza], tags=["Poliza"])
def obtener_polizas():
    '''
    Metodo para obtener todas las polizas registradas de un seguro
    de la base de datos.

    En caso de obtenerlas correctamente retorna una lista de
    objetos de Poliza.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    resultados = conexion.execute(polizas.select()).fetchall()
    conexion.close()
    if resultados:
        return resultados

    raise HTTPException(status_code=404, detail="No se encontraron polizas")


@ruta_poliza.get('/polizas/usuario', response_model=list[Poliza], tags=["Poliza"])
def obtener_polizas_usuario(id_conductor: int):
    '''
    Metodo para obtener todas las polizas registradas de un usuario
    de la base de datos.

    En caso de obtenerlas correctamente retorna una lista de
    objetos de Poliza.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    resultados = conexion.execute(polizas.select().where(polizas.c.idConductor == id_conductor)).fetchall()
    conexion.close()
    if resultados:
        return resultados

    raise HTTPException(status_code=404, detail="No se encontraron polizas")


@ruta_poliza.get('/polizas/idPoliza', response_model=int, tags=['Poliza'])
def obtener_poliza_id_vehiculo(id_vehiculo: int):
    '''
    Metodo para obtener una poliza de seguro de un coductor
    dato el id del vehiculo asociado.

    En caso de obtener bien la poliza retorna un codigo 200.

    En caso contrario retorna un codigo 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(polizas.select().where(polizas.c.idVehiculo == id_vehiculo)).first()
    conexion.close()
    if resultado:
        return resultado[0]
    
    raise HTTPException(status_code=404, detail="No se encontro la poliza")



@ruta_poliza.post('/poliza', status_code=HTTP_200_OK, tags=["Poliza"])
def agregar_poliza(poliza: Poliza):
    '''
    Metodo para agregar una poliza de seguro de un coductor
    a la base de datos .

    En caso de registrar bien el poliza retorna un codigo 200.

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(polizas.insert().values(poliza.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al registrar poliza")


@ruta_poliza.put('/poliza', status_code=HTTP_200_OK, tags=["Poliza"])
def actualizar_poliza(poliza: Poliza, id_poliza: int):
    '''
    Metodo para actualizar un  una poliza de seguro de un conductor.

    En caso de actualizar correctamente la poliza retorna un codigo 200

    En caso contrario retorna un codigo 500.
    '''

    conexion = conexionDb()
    resultado = conexion.execute(polizas.update().values(
        idpoliza=id_poliza,
        idConductor=poliza.idConductor,
        idVehiculo=poliza.idVehiculo,
        fechaInicio=poliza.fechaInicio,
        plazo=poliza.plazo,
        tipoCobertura=poliza.tipoCobertura,
        costo=poliza.costo,
        fechaFin=poliza.fechaFin
    ).where(polizas.c.idpoliza == id_poliza))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al actualizar poliza")


@ruta_poliza.delete('/poliza', status_code=HTTP_204_NO_CONTENT, tags=["Poliza"])
def eliminar_poliza(id_poliza: int):
    '''
    Metodo para eliminar una poliza de seguro de un conductor
    de la base de datos.

    En caso de eliminar correctamente la poliza retorna un codigo 204

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(polizas.delete().where(
        polizas.c.idpoliza == id_poliza))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=500, detail="Error del servidor al eliminar poliza")
