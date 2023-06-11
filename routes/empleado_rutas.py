from fastapi import APIRouter, HTTPException, Response
from models.empleado import Empleado
from config.db import conexionDb
from schemas.empleado_esquema import empleados
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from security.encriptacion import cargar_llave, desencriptar_contenido
from middlewares.verificar_token_rutas import VerificarTokenRutas

ruta_empleado = APIRouter(route_class=VerificarTokenRutas)


@ruta_empleado.get('/empleado', response_model=Empleado, tags=["Empleado"])
def obtener_empleado(id_empleado: int):
    '''
    Ruta para obtener informacion de un empleado especifico dado el id de 
    un empleado.

    El id del empleado recibido debe ser de tipo int para no producir un error
    en el servidor.

    En el caso de que la consulta sea exitosa se retornara el empleado encontrado
    en el caso de que la busqueda sea en vano el servidor retornara un 404 con el
    mensaje "empleado no encontrado".
    '''

    conexion = conexionDb()
    resultado = conexion.execute(empleados.select().where(
        empleados.c.idEmpleado == id_empleado)).first()
    conexion.close()
    if resultado:
        empleadoObtenido = Empleado(
            idEmpleado=resultado[0], nombreCompleto=resultado[1], fechaIngreso=resultado[2], cargo=resultado[3], nombreUsuario=resultado[4], contrasena=resultado[5])
        empleadoObtenido.decodificar_informacion()
        return empleadoObtenido

    raise HTTPException(status_code=404, detail="Empleado no encontrado")


@ruta_empleado.get('/empleados', response_model=list[Empleado], tags=["Empleado"])
def obtener_empleados():
    '''
    Ruta para obtener todos los empleados registrados en la base de datos

    El metodo retorna una lista de objetos Empleado, con todos los\n
    empleados que haya obtenido de la base de datos
    '''

    conexion = conexionDb()
    empleados_obtenidos: list[Empleado] = []
    resultados = conexion.execute(empleados.select()).fetchall()
    conexion.close()
    if resultados:
        for fila in resultados:
            empleado_obtenido = Empleado(idEmpleado=fila[0], nombreCompleto=fila[1], fechaIngreso=fila[2], cargo=fila[3], nombreUsuario=fila[4], contrasena=fila[5])
            empleado_obtenido.decodificar_informacion()
            empleados_obtenidos.append(empleado_obtenido)

        return empleados_obtenidos

    raise HTTPException(status_code=404, detail="No se encontraron empleados")


@ruta_empleado.post('/empleado', status_code=HTTP_200_OK, tags=["Empleado"])
def agregar_empleado(empleado: Empleado):
    '''
    Ruta para agregar un empleado a la base de datos, recibe un \n
    objeto de tipo Empleado y lo agrega a la base de datos.\n

    Si el registro es exitoso se retorna un objeto de tipo Response\n
    con un status code 200.

    Si ocurre un error a la hora de registra el empleado, se retorna
    un codigo 500.
    '''

    conexion = conexionDb()
    empleado.codificar_informacion()
    resultado = conexion.execute(empleados.insert().values(empleado.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al registrar empleado")


@ruta_empleado.post('/authEmpleado', status_code=HTTP_200_OK, tags=["Empleado"])
def autenticar_empleado(empleado: Empleado):
    '''
    Este metodo se encarga de autenticar que se reciba un empleado
    valido para el inicio de sesion.

    En el caso de que el empleado sea valido el metodo retornara
    un codigo HTTP 200.

    En el caso de no encontrar al empleado solicitado se retornara
    un codigo 500 de que no se encontro al empleado solicitado.

    En el caso de que el empleado se encontro pero no coincide la
    contraseña otorgada se retornara un http 401 con el mensaje
    empleado no valido
    '''

    conexion = conexionDb()
    resultado = conexion.execute(empleados.select().where(
        empleados.c.nombreUsuario == empleado.nombreUsuario)).first()
    if resultado:
        empleadoObtenido: Empleado = resultado

        llave = cargar_llave()
        contrasena_obtenida = desencriptar_contenido(
            empleadoObtenido.contrasena.encode(), llave)

        if empleado.contrasena == contrasena_obtenida:
            return Response(status_code=HTTP_200_OK)

        raise HTTPException(status_code=401, detail="Empleado no valido")

    raise HTTPException(
        status_code=500, detail="Empleado solicitado no encontrado")


@ruta_empleado.put('/empleado', status_code=HTTP_200_OK, tags=["Empleado"])
def actualizar_empleado(empleado: Empleado, id_empleado: int):
    '''
    Ruta para actualizar la informacion de un empleado dado el id del empleado.

    El metodo recibe un objeto de tipo empleado y un id de empleado de tipo int
    para su funcionamiento correcto

    En caso de que la actualizacion de datos sea correcta el servidor retornara un
    HTTP 200, en el caso contrario retornara un HTTP 500
    '''

    conexion = conexionDb()
    empleado.codificar_informacion()
    resultado = conexion.execute(empleados.update().values(
        idEmpleado=id_empleado,
        nombreCompleto=empleado.nombreCompleto,
        fechaIngreso=empleado.fechaIngreso,
        cargo=empleado.cargo,
        nombreUsuario=empleado.nombreUsuario,
        contrasena=empleado.contrasena
    ).where(empleados.c.idEmpleado == id_empleado))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)

    raise HTTPException(
        status_code=500, detail="Error del servidor al actualizar empleado")


@ruta_empleado.delete('/empleado', status_code=HTTP_204_NO_CONTENT, tags=["Empleado"])
def eliminar_empleado(id_empleado: str):
    '''
    Ruta para la eliminacion de un empleado de la base de datos dado el id del empleado.

    El id del empleado que recibe debe ser un tipo de dato int.

    En caso de que la eliminacion sea exitosa el servidor retornara un codigo HTTP 204,
    en el caso contrario el servidor retornara un HTTP 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(empleados.delete().where(
        empleados.c.idEmpleado == id_empleado))
    conexion.close()
    conexion.commit()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=500, detail="Error del servidor al eliminar empleado")
