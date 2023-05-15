from fastapi import APIRouter, HTTPException, Response
from models.conductor import Conductor
from config.db import conexionDb
from schemas.conductor_esquema import conductores
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK


ruta_conductor = APIRouter()

@ruta_conductor.get('/conductor', response_model=Conductor, tags=["Conductor"])
def obtener_conductor(id_conductor: int):
    conexion = conexionDb()
    resultado = conexion.execute(conductores.select().where(
        conductores.c.idConductor == id_conductor)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail='Conductor no encontrado')


@ruta_conductor.post('/conductor', status_code=HTTP_200_OK, tags=["Conductor"])
def agregar_conductor(conductor: Conductor):
    conexion = conexionDb()
    resultado = conexion.execute(conductores.insert().values(conductor))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail='Error de registro en el servidor')


@ruta_conductor.put('/conductor', status_code=HTTP_200_OK, tags=["Conductor"])
def actualizar_conductor(conductor: Conductor, id_conductor: int):
    conexion = conexionDb()
    resultado = conexion.execute(conductores.update().values(
        idConductor = id_conductor,
        nombreCompleto = conductor.nombreCompleto,
        numLicencia = conductor.numLicencia,
        fechaNacimiento = conductor.fechaNacimiento,
        telefono = conductor.telefono,
        contrasena = conductor.contrasena
    ).where(conductores.c.idConductor == id_conductor))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar")


@ruta_conductor.delete('/conductor', status_code=HTTP_204_NO_CONTENT, tags=["Conductor"])
def eliminar_conductor(id_conductor: int):
    conexion = conexionDb()
    resultado = conexion.execute(conductores.delete().where(
        conductores.c.idConductor == id_conductor))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar conductor")