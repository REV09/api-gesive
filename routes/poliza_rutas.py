from fastapi import APIRouter, HTTPException, Response
from models.poliza import Poliza
from config.db import conexionDb
from schemas.poliza_esquema import polizas
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_poliza = APIRouter()

@ruta_poliza.get('/poliza', response_model=Poliza, tags=["Poliza"])
def obtener_vehiculo(id_poliza: int):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.select().where(
        polizas.c.idVehiculo == id_poliza)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="poliza no encontrada")


@ruta_poliza.post('/poliza', status_code=HTTP_200_OK, tags=["Poliza"])
def agregar_vehiculo(poliza: Poliza):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.insert().values(poliza))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar poliza")


@ruta_poliza.put('/poliza', status_code=HTTP_200_OK, tags=["Poliza"])
def actualizar_vehiculo(poliza: Poliza, id_poliza: int):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.update().values(
        idPoliza = id_poliza,
        idConductor = poliza.idConductor,
        idVehiculo = poliza.idVehiculo,
        fechaInicio = poliza.fechaInicio,
        plazo = poliza.plazo,
        tipoCobertura = poliza.tipoCobertura,
        costo = poliza.costo,
        fechaFin = poliza.fechaFin
    ).where(polizas.c.idPoliza == id_poliza))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar poliza")


@ruta_poliza.delete('/poliza', status_code=HTTP_204_NO_CONTENT, tags=["Poliza"])
def eliminar_vehiculo(id_poliza: int):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.delete().where(
        polizas.c.idPoliza == id_poliza))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar poliza")
 