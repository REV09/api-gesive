from fastapi import APIRouter, HTTPException, Response
from models.empleado import Empleado
from config.db import conexionDb
from schemas.empleado_esquema import empleados
from starlette.status import HTTP_204_NO_CONTENT, HTTP_200_OK


ruta_empleado =  APIRouter()

@ruta_empleado.get('/empleado', response_model=Empleado, tags=["Empleado"])
def obtener_empleado(id_empleado: int):
    conexion = conexionDb()
    resultado = conexion.execute(empleados.select().where(
        empleados.c.idEmpleado == id_empleado)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

@ruta_empleado.get('/empleados', response_model=list[Empleado], tags=["Empleado"])
def obtener_empleados():
    conexion = conexionDb()
    resultados = conexion.execute(empleados.select()).fetchall()
    conexion.close()
    if resultados:
        return resultados
    
    raise HTTPException(status_code=404, detail="No se encontraron empleados")


@ruta_empleado.post('/empleado', status_code=HTTP_200_OK, tags=["Empleado"])
def agregar_empleado(empleado: Empleado):
    conexion = conexionDb()
    resultado = conexion.execute(empleados.insert().values(empleado.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar empleado")


@ruta_empleado.post('/authEmpleado', status_code=HTTP_200_OK, tags=["Empleado"])
def autenticar_empleado(empleado: Empleado):
    conexion = conexionDb()
    resultado = conexion.execute(empleados.select().where(
        empleados.c.nombreUsuario == empleado.nombreUsuario)).first()
    if resultado:
        empleadoObtenido: Empleado = resultado

        if empleado.contrasena == empleadoObtenido.contrasena:
            return Response(status_code=HTTP_200_OK)
        
        raise HTTPException(status_code=401, detail="Empleado no valido")
    
    raise HTTPException(status_code=500, detail="Empleado solicitado no encontrado")


@ruta_empleado.put('/empleado', status_code=HTTP_200_OK, tags=["Empleado"])
def actualizar_empleado(empleado: Empleado, id_empleado: int):
    conexion = conexionDb()
    resultado = conexion.execute(empleados.update().values(
        idEmpleado = id_empleado,
        nombreCompleto = empleado.nombreCompleto,
        fechaIngreso = empleado.fechaIngreso,
        cargo = empleado.cargo,
        nombreUsuario = empleado.nombreUsuario,
        contrasena = empleado.contrasena
    ).where(empleados.c.idEmpleado == id_empleado))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar empleado")


@ruta_empleado.delete('/empleado', status_code=HTTP_204_NO_CONTENT, tags=["Empleado"])
def eliminar_empleado(id_empleado: str):
    conexion = conexionDb()
    resultado = conexion.execute(empleados.delete().where(
        empleados.c.idEmpleado == id_empleado))
    conexion.close()
    conexion.commit()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar empleado")