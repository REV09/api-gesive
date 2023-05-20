from fastapi import APIRouter, HTTPException, Response
from models.conductor import Conductor
from config.db import conexionDb
from schemas.conductor_esquema import conductores
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK


ruta_conductor = APIRouter()

@ruta_conductor.get('/conductor', response_model=Conductor, tags=["Conductor"])
def obtener_conductor(id_conductor: int):

    '''
    Ruta para obtener informacion de un conductor especifico dado el id de 
    un conductor.

    El id del conductor recibido debe ser de tipo int para no producir un error
    en el servidor.

    En el caso de que la consulta sea exitosa se retornara el conductor encontrado
    en el caso de que la busqueda sea en vano el servidor retornara un 404 con el
    mensaje "Conductor no encontrado".
    '''

    conexion = conexionDb()
    resultado = conexion.execute(conductores.select().where(
        conductores.c.idConductor == id_conductor)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail='Conductor no encontrado')


@ruta_conductor.post('/conductor', status_code=HTTP_200_OK, tags=["Conductor"])
def agregar_conductor(conductor: Conductor):

    '''
    Ruta para agregar un conductor a la base de datos.

    Recibe un objeto de tipo Conductor, para agregarlo a la tabla conductor en la
    base de datos.

    Si el conductor es registrado con exito el servidor retornara n HTTP 200, en
    caso de que ocurra lo contrario este retornara un HTTP 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(conductores.insert().values(conductor.dict()))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail='Error de registro en el servidor')


@ruta_conductor.put('/conductor', status_code=HTTP_200_OK, tags=["Conductor"])
def actualizar_conductor(conductor: Conductor, id_conductor: int):

    '''
    Ruta para actualizar la informacion de un conductor dado el id del conductor.

    El metodo recibe un objeto de tipo Conductor y un id de conductor de tipo int
    para su funcionamiento correcto

    En caso de que la actualizacion de datos sea correcta el servidor retornara un
    HTTP 200, en el caso contrario retornara un HTTP 500
    '''

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

    '''
    Ruta para la eliminiacion de un coductor de la base de datos dado el id del conductor.

    El id del conductor que recibe debe ser un tipo de dato int.

    En caso de que la eliminacion sea exitosa el servidor retornara un codigo HTTP 204,
    en el caso contrario el servidor retornara un HTTP 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(conductores.delete().where(
        conductores.c.idConductor == id_conductor))
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar conductor")