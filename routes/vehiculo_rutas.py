from fastapi import APIRouter, HTTPException, Response
from models.vehiculo import Vehiculo
from config.db import conexionDb
from schemas.vehiculo_esquema import vehiculos
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_vehiculo = APIRouter()

@ruta_vehiculo.get('/vehiculo', response_model=Vehiculo, tags=["Vehiculo"])
def obtener_vehiculo(id_vehiculo: int):
    conexion = conexionDb()
    resultado = conexion.execute(vehiculos.select().where(
        vehiculos.c.idVehiculo == id_vehiculo)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")


@ruta_vehiculo.post('/vehiculo', status_code=HTTP_200_OK, tags=["Vehiculo"])
def agregar_vehiculo(vehiculo: Vehiculo):
    conexion = conexionDb()
    resultado = conexion.execute(vehiculos.insert().values(vehiculo))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar vehiculo")


@ruta_vehiculo.put('/vehiculo', status_code=HTTP_200_OK, tags=["Vehiculo"])
def actualizar_vehiculo(vehiculo: Vehiculo, id_vehiculo: int):
    conexion = conexionDb()
    resultado = conexion.execute(vehiculos.update().values(
        idVehiculo = id_vehiculo,
        numeroSerie = vehiculo.numeroSerie,
        anio = vehiculo.anio,
        marca = vehiculo.marca,
        modelo = vehiculo.modelo,
        color = vehiculo.color,
        numPlacas = vehiculo.numPlacas
    ).where(vehiculos.c.idVehiculo == id_vehiculo))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar vehiculo")


@ruta_vehiculo.delete('/vehiculo', status_code=HTTP_204_NO_CONTENT, tags=["Vehiculo"])
def eliminar_vehiculo(id_vehiculo: int):
    conexion = conexionDb()
    resultado = conexion.execute(vehiculos.delete().where(
        vehiculos.c.idConductor == id_vehiculo))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar vehiculo")
 