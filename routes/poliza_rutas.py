from fastapi import APIRouter, HTTPException, Response
from models.poliza import Poliza
from config.db import conexionDb
from schemas.poliza_esquema import polizas
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_poliza = APIRouter()

@ruta_poliza.get('/poliza', response_model=Poliza, tags=["Poliza"])
def obtener_poliza(id_poliza: int):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.select().where(
        polizas.c.idpoliza == id_poliza)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="poliza no encontrada")


@ruta_poliza.get('/polizas', response_model=list[Poliza], tags=["Poliza"])
def obtener_polizas():
    conexion = conexionDb()
    resultados = conexion.execute(polizas.select()).fetchall()
    conexion.close()
    if resultados:
        return resultados
    
    raise HTTPException(status_code=404, detail="No se encontraron polizas")


@ruta_poliza.post('/poliza', status_code=HTTP_200_OK, tags=["Poliza"])
def agregar_poliza(poliza: Poliza):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.insert().values(poliza.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar poliza")


@ruta_poliza.put('/poliza', status_code=HTTP_200_OK, tags=["Poliza"])
def actualizar_poliza(poliza: Poliza, id_poliza: int):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.update().values(
        idpoliza = id_poliza,
        idConductor = poliza.idConductor,
        idVehiculo = poliza.idVehiculo,
        fechaInicio = poliza.fechaInicio,
        plazo = poliza.plazo,
        tipoCobertura = poliza.tipoCobertura,
        costo = poliza.costo,
        fechaFin = poliza.fechaFin
    ).where(polizas.c.idpoliza == id_poliza))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar poliza")


@ruta_poliza.delete('/poliza', status_code=HTTP_204_NO_CONTENT, tags=["Poliza"])
def eliminar_poliza(id_poliza: int):
    conexion = conexionDb()
    resultado = conexion.execute(polizas.delete().where(
        polizas.c.idpoliza == id_poliza))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar poliza")
 