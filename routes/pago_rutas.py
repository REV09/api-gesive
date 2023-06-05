from fastapi import APIRouter, HTTPException, Response
from models.pago import Pago
from config.db import conexionDb
from schemas.pago_esquema import pagos
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_pagos = APIRouter()

@ruta_pagos.get('/pago', response_model=Pago, tags=["Pago"])
def obtener_pago(id_pago: int):

    '''
    Ruta para obtener el pago de una poliza de seguro de un conductor.

    Recibe el id del pago de tipo int para la busqueda.

    En caso de encontrar el pago lo retorna, sino retorna un
    codigo 404
    '''

    conexion = conexionDb()
    resultado = conexion.execute(pagos.select().where(
        pagos.c.idPago == id_pago)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="Pago no encontrado")


@ruta_pagos.post('/pago', status_code=HTTP_200_OK, tags=["Pago"])
def agregar_pago(pago: Pago):

    '''
    Metodo para agregar un pago de poliza de seguro de un coductor
    a la base de datos .

    En caso de registrar bien el pago retorna un codigo 200.

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(pagos.insert().values(pago.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar Pago")


@ruta_pagos.put('/pago', status_code=HTTP_200_OK, tags=["Pago"])
def actualizar_pago(pago: Pago, id_pago: int):

    '''
    Metodo para actualizar un pago de una poliza de seguro de un conductor.

    En caso de actualizar correctamente el pago retorna un codigo 200

    En caso contrario retorna un codigo 500.
    '''

    conexion = conexionDb()
    resultado = conexion.execute(pagos.update().values(
        idPago = id_pago,
        idPoliza = pago.idPoliza,
        idConductor = pago.idConductor,
        monto = pago.monto,
        fecha = pago.fecha,
        formaDePago = pago.formaDePago,
        numeroTarjeta = pago.numeroTarjeta,
        fechaVencimiento = pago.fechaVencimiento,
        cvv = pago.cvv
    ).where(pagos.c.idPago == id_pago))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al actualizar Pago")


@ruta_pagos.delete('/pago', status_code=HTTP_204_NO_CONTENT, tags=["Pago"])
def eliminar_pago(id_pago: int):

    '''
    Metodo para eliminar un pago de una poliza de seguro de un conductor
    de la base de datos.

    En caso de eliminar correctamente el pago retorna un codigo 204

    En caso contrario retorna un codigo 500
    '''

    conexion = conexionDb()
    resultado = conexion.execute(pagos.delete().where(
        pagos.c.idPago == id_pago))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar Pago")
 