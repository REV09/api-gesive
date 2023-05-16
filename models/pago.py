from pydantic import BaseModel
from datetime import date

class Pago(BaseModel):
    idPago: int
    idPoliza: int
    idConductor: int
    monto: float
    fecha: date
    formaDePago: bool
    numeroTarjeta: str
    fechaVencimiento: str
    cvv: str

    class Config:
        orm_mode = True