from fastapi import APIRouter, HTTPException, Response
from models.vehiculo import Vehiculo
from config.db import conexionDb
from schemas.vehiculo_esquema import vehiculos
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from middlewares.verificar_token_rutas import VerificarTokenRutas
from models.vehiculo import Vehiculo


ruta_vehiculo = APIRouter(route_class=VerificarTokenRutas)


@ruta_vehiculo.get('/vehiculo', response_model=Vehiculo, tags=["Vehiculo"])
def obtener_vehiculo(id_vehiculo: int):
    '''
    Ruta para obtener un vehiculo de un coductor dado el id del vehiculo.

    Recibe el id del vehiculo de tipo int para la busqueda.

    En caso de encontrar el vehiculo lo retorna, sino retorna un
    codigo 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(vehiculos.select().where(
        vehiculos.c.idvehiculo == id_vehiculo)).first()
    conexion.close()
    if resultado:
        vehiculo_obtenido = Vehiculo(idvehiculo=resultado[0], numeroSerie=resultado[1],
                                     anio=resultado[2], marca=resultado[3],
                                     modelo=resultado[4], color=resultado[5],
                                     numPlacas=resultado[6])

        vehiculo_obtenido.decodificar_informacion()
        return vehiculo_obtenido

    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")


@ruta_vehiculo.post('/vehiculo', status_code=HTTP_200_OK, tags=["Vehiculo"])
def agregar_vehiculo(vehiculo: Vehiculo):
    '''
    Metodo para agregar un vehiculo de un coductor
    a la base de datos .

    En caso de registrar bien el vehiculo retorna un codigo 200.

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    vehiculo.codificar_informacion()
    resultado = conexion.execute(vehiculos.insert().values(vehiculo.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al registrar vehiculo")


@ruta_vehiculo.put('/vehiculo', status_code=HTTP_200_OK, tags=["Vehiculo"])
def actualizar_vehiculo(vehiculo: Vehiculo, id_vehiculo: int):
    '''
    Metodo para actualizar un vehiculo de un conductor.

    En caso de actualizar correctamente el vehiculo retorna un codigo 200

    En caso contrario retorna un codigo 500.
    '''

    conexion = conexionDb()
    vehiculo.codificar_informacion()
    resultado = conexion.execute(vehiculos.update().values(
        idvehiculo=id_vehiculo,
        numeroSerie=vehiculo.numeroSerie,
        anio=vehiculo.anio,
        marca=vehiculo.marca,
        modelo=vehiculo.modelo,
        color=vehiculo.color,
        numPlacas=vehiculo.numPlacas
    ).where(vehiculos.c.idvehiculo == id_vehiculo))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al actualizar vehiculo")


@ruta_vehiculo.delete('/vehiculo', status_code=HTTP_204_NO_CONTENT, tags=["Vehiculo"])
def eliminar_vehiculo(id_vehiculo: int):
    '''
    Metodo para eliminar un vehiculo de un conductor
    de la base de datos.

    En caso de eliminar correctamente el vehiculo retorna un codigo 204

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(vehiculos.delete().where(
        vehiculos.c.idvehiculo == id_vehiculo))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=500, detail="Error del servidor al eliminar vehiculo")
