from pydantic import BaseModel
from datetime import datetime

from security.encriptacion import cargar_llave, desencriptar_contenido, encriptar_contenido

class Pago(BaseModel):
    idPago: int
    idPoliza: int
    idConductor: int
    monto: float
    fecha: datetime
    formaDePago: bool
    numeroTarjeta: str
    fechaVencimiento: str
    cvv: str

    class Config:
        orm_mode = True

    def codificar_informacion(self):
        llave = cargar_llave()
        self.numeroTarjeta = encriptar_contenido(self.numeroTarjeta, llave).decode()
        self.fechaVencimiento = encriptar_contenido(self.fechaVencimiento, llave).decode()
        self.cvv = encriptar_contenido(self.cvv, llave).decode()


    def decodificar_informacion(self):
        llave = cargar_llave()
        self.numeroTarjeta = desencriptar_contenido(self.numeroTarjeta.encode(), llave)
        self.fechaVencimiento = desencriptar_contenido(self.fechaVencimiento.encode(), llave)
        self.cvv = desencriptar_contenido(self.cvv.encode(), llave)