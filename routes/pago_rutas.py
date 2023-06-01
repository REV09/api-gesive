from fastapi import APIRouter, HTTPException, Response
from models.pago import Pago
from config.db import conexionDb
from schemas.pago_esquema import pagos
from starlette.status import HTTP_200_OK, HTTP_204_NO_CONTENT


ruta_pagos = APIRouter()

@ruta_pagos.get('/pago', response_model=Pago, tags=["Pago"])
def obtener_pago(id_pago: int):
    conexion = conexionDb()
    resultado = conexion.execute(pagos.select().where(
        pagos.c.idPago == id_pago)).first()
    conexion.close()
    if resultado:
        return resultado
    
    raise HTTPException(status_code=404, detail="Pago no encontrado")


@ruta_pagos.post('/pago', status_code=HTTP_200_OK, tags=["Pago"])
def agregar_pago(pago: Pago):
    conexion = conexionDb()
    resultado = conexion.execute(pagos.insert().values(pago.dict()))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_200_OK)
    
    raise HTTPException(status_code=500, detail="Error del servidor al registrar Pago")


@ruta_pagos.put('/pago', status_code=HTTP_200_OK, tags=["Pago"])
def actualizar_pago(pago: Pago, id_pago: int):
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
    conexion = conexionDb()
    resultado = conexion.execute(pagos.delete().where(
        pagos.c.idPago == id_pago))
    conexion.commit()
    conexion.close()
    if resultado:
        return Response(status_code=HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=500, detail="Error del servidor al eliminar Pago")
 